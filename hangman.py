import random
import string
HANGMANPICS = ['''
  _____
  |   |
      |
      |
      |
      |
=========''', '''
  _____
  |   |
  O   |
      |
      |
      |
=========''', '''
  _____
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  _____
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  _____
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  _____
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  _____
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def getRandomWord():
  text_file = open("dictionary.txt", "r")
  word = text_file.readlines()
  return random.choice(word).strip()

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print 'Missed letters:',
    for letter in missedLetters:
        print letter, " "
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks: # show the secret word with spaces in between each letter
        print letter,
already_guessed = []
def getGuess(alreadyGuessed):
    while True:
      guess = raw_input("Pick a letter: ").lower()
      if guess == "quit":
        exit()
      if len(guess) == 1 and guess in string.ascii_lowercase and guess not in already_guessed:
        break
    already_guessed.append(guess)
    return guess

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord()
gameIsDone = False
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
           break
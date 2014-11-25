import random
import os
import time
import string

hangmanImages = ['''
 ________
 |/     :
 |      :
 |
 |
/|\\
===========
''',
'''
 ________
 |/     :
 |      o
 |
 |
/|\\
===========
''',
'''
 ________
 |/     :
 |      o
 |      |
 |
/|\\
===========
''',
'''
 ________
 |/     :
 |      o
 |     /|
 |
/|\\
===========
''',
'''
 ________
 |/     :
 |      o
 |     /|\\
 |
/|\\
===========
''',
'''
 ________
 |/     :
 |      o
 |     /|\\
 |     /
/|\\
===========
''',
'''
 ________
 |/     :
 |      o
 |     /|\\
 |     / \\
/|\\
===========
'''
]

def getRandomWord():
	text_file = open("dictionary.txt", "r")
	word = text_file.readlines()
	return random.choice(word).strip()

	return random.choice(words)

word = getRandomWord()

def draw(misses):
	print(hangmanImages[misses])

total_misses = len(hangmanImages) - 1

for i in range(len(hangmanImages)):
	print(word)
 	draw(i)
	time.sleep(1)
	os.system("cls")

def get_guess():
	while True:
		guess = raw_input("Pick a letter: ").lower()
		if guess == "quit":
			exit()
		if len(guess) == 1 and guess in string.ascii_lowercase and guess not in already_guessed:
			break
	already_guessed = []
	already_guessed.append(guess)
	return guess

get_guess()
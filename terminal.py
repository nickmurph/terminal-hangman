#functions and vars for terminal manipulation and printing
#functions for manipulating data and repetitive actions

import os 

alphabet ="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

def clear_terminal():
	os.system('clear')

def print_buffer():
	print("")
	print("")
	print("")

def print_header():
	print(header_logo)
	
def validate_input(guess):
	if len(guess) == 1 and guess in alphabet:
		return True
	else:
		return -1

def validation_loop(turn):
	if turn == 1:
		guess = input("Enter your first letter guess: ")
	
	else:
		guess = input("Enter your next letter guess: ")

	while (validate_input(guess) != True):
		guess = input("Invalid input, enter a letter only:")
	return guess

def print_word_progress(wordArray):
	print(" ".join(wordArray))


header_logo = """
 _   _   ____   __  _  ____  __  __   ____   __  _
| |_| | / () \ |  \| |/ (_,`|  \/  | / () \ |  \| |
|_| |_|/__/\__\|_|\__|\____)|_|\/|_|/__/\__\|_|\__|

"""



hangman11 = """

	    --------
	    |      |
	    |      |
	    O      |
	    |      |
	   /|\     |
	    |      |
	    |      |
	   / \     |
		   |
	============


"""

hangman10 = """

	    --------
	    |      |
	    |      |
	    O      |
	    |      |
	   /|\     |
	    |      |
	    |      |
	     \     |
		   |
	============


"""
hangman9 = """

	    --------
	    |      |
	    |      |
	    O      |
	    |      |
	   /|\     |
	    |      |
	    |      |
	           |
		   |
	============


"""
hangman8 = """

	    --------
	    |      |
	    |      |
	    O      |
	    |      |
	   /|\     |
	    |      |
	           |
	           |
		   |
	============


"""

hangman7 = """

	    --------
	    |      |
	    |      |
	    O      |
	    |      |
	   /|\     |
	           |
	           |
	           |
		   |
	============


"""
hangman6 = """

	    --------
	    |      |
	    |      |
	    O      |
	    |      |
	   /|      |
	           |
	           |
	           |
		   |
	============


"""
hangman5 = """

	    --------
	    |      |
	    |      |
	    O      |
	    |      |
	    |      |
	           |
	           |
	           |
		   |
	============


"""
hangman4 = """

	    --------
	    |      |
	    |      |
	    O      |
	    |      |
	           |
	           |
	           |
	           |
		   |
	============


"""
hangman3 = """

	    --------
	    |      |
	    |      |
	    O      |
	           |
	           |
	           |
	           |
	           |
		   |
	============


"""

hangman2 = """

	    --------
	    |      |
	    |      |
	           |
	           |
	           |
	           |
	           |
	           |
		   |
	============


"""

hangman1 = """

	    --------
	    |      |
	           |
	           |
	           |
	           |
	           |
	           |
	           |
		   |
	============


"""

hangman0 = """

	    --------
	           |
	           |
	           |
	           |
	           |
	           |
	           |
	           |
		   |
	============


"""
hangman_list = [hangman0,hangman1,hangman2,hangman3,hangman4,hangman5,hangman6,hangman7,hangman8,hangman9,hangman10,hangman11]

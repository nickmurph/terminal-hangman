#functions and vars for terminal manipulation and printing
import os 


def clear_terminal():
	os.system('clear')

def print_buffer():
	print("")
	print("")
	print("")

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
#for x in hangman_list:
#	print(x)

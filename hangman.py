import os
import random
from curated_list import return_curated_list
from terminal import *



wordList = return_curated_list()
wordListLen = len(wordList)



wordIndex = random.randint(0, wordListLen-1)
curWord = wordList[wordIndex].upper()
wordLength = len(curWord)
roundFlag = True
guessCount = 0

word_array = []
for i in range(wordLength):
	word_array.append(" _ ")

def clear_and_print_game():
	clear_terminal()
	print_header()
	print(hangman_list[guessCount])
	print_word_progress(word_array)
	print_buffer()

def evaluate_guess():
	global guessCount
	global guess
	guess = guess.upper()
	for i in range(wordLength):
		if curWord[i] == guess:
			word_array[i] = " " + guess + " "
	if guess not in curWord:
		guessCount = guessCount+1


def reset_round():
	global wordIndex
	global curWord
	global wordLength
	global roundFlag
	global guessCount
	global word_array
	wordIndex = random.randint(0, wordListLen-1)
	curWord = wordList[wordIndex].upper()
	wordLength = len(curWord)
	guessCount = 0
	word_array = []
	for i in range(wordLength):
		word_array.append(" _ ")


clear_terminal()
print_header()
print(hangman_list[11])


input("Press any key to begin the game: ")

clear_and_print_game()


guess = validation_loop(1)
evaluate_guess()
clear_and_print_game()

while(roundFlag):
	guess = validation_loop(2)
	evaluate_guess()
	clear_and_print_game()

	if " _ " not in word_array:
		print("Congratulations, you guessed the word correctly!")
		newRound = input("Would you like to play another round? (y/n)")

		if newRound.upper() in ["Y", "YES"]:
			reset_round()
			clear_and_print_game()
		else:
			roundFlag = False

	if guessCount >= 11:
		print(f"You failed to guess the word in time! The word was {curWord}")
		newRound = input("Would you like to play another round? (y/n)")

		if newRound.upper() in ["Y","YES"]:
			reset_round()
			clear_and_print_game()

		else:
			roundFlag = False

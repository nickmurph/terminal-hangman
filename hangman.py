#testing python in Ubuntu via Windows Subsystem for Linux
#dinky testing has now evolved into a full-on implementation of Hangman...because why not
import random
import os
from curated_list import return_curated_list
#from terminal import clear_terminal, print_buffer, print_header, validate_input, validation_loop, hangman_list
from terminal import *


# temp word list used for testing
#wordList = ["spurious", "byzantine", "zoonotically", "obstetrician", "defenestrate", "ostracize"]


wordList = return_curated_list()
wordListLen = len(wordList)



wordIndex = random.randint(0, wordListLen-1)
curWord = wordList[wordIndex]
wordLength = len(curWord)

word_array = []
for i in range(wordLength):
	word_array.append(" _ ")

clear_terminal()
print_header()
print(hangman_list[11])

print_buffer()
input("Press any key to begin the game: ")

clear_terminal()
print_header()
print(hangman_list[0])
print_word_progress(word_array)

print_buffer()

guess = validation_loop(1)
for i in range(wordLength):
	if curWord[i] == guess:
		word_array[i] = " " + guess + " "

roundFlag = True
guessCount = 0
while (roundFlag):
	guess = validation_loop(guessCount)
	for i in range(wordLength):
		if curWord[i] == guess:
			word_array[i] = " " + guess + " "
	if guess not in curWord:
		guessCount = guessCount+1


	clear_terminal()
	print_header()
	print(hangman_list[guessCount])
	print_word_progress(word_array)
	
	#TODO: check if the word has been fully guessed
	#TODO: if it has, initiate victory message and replay query
	#if it hasn't, following code will let loop progress or end it if guess limit reached
	#if guessCount >= wordLength:
	if guessCount >= 11:
		roundFlag = False

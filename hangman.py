#testing python in Ubuntu via Windows Subsystem for Linux
#dinky testing has now evolved into a full-on implementation of Hangman...because why not
import random
import os
from curated_list import return_curated_list
from terminal import clear_terminal, print_buffer, header_logo, hangman_list



clear_terminal()
print(header_logo)
print(hangman_list[11])

# temp word list used for testing
#wordList = ["spurious", "byzantine", "zoonotically", "obstetrician", "defenestrate", "ostracize"]

wordList = return_curated_list()
wordListLen = len(wordList)
wordIndex = random.randint(0, wordListLen-1)
curWord = wordList[wordIndex]
wordLength = len(curWord)


print_buffer()
input("Press any key to begin the game: ")

clear_terminal()
print(header_logo)
print(hangman_list[0])


for i in range(wordLength):
	print(" _ ", end="")

print_buffer()
guess = input("Enter your first letter guess: ")

gameFlag = True
guessCount = 1
while (gameFlag):
	guess = input ("Enter your next letter guess: ")
	#TODO: check if the letter is a correct guess
	#TODO: if it is, fill in the letter(s) on the screen
	guessCount = guessCount+1
	#TODO: check if the word has been fully guessed
	#TODO: if it has, initiate victory message and replay query
	#if it hasn't, following code will let loop progress or end it if guess limit reached
	if guessCount >= wordLength:
		gameFlag = False

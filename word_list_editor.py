# taking the word list from usr/shared/dict/ and trimming it down per Hangman needs
# this was a fun approach, but the words list is too broad in scope. Even with filtering out redundant possessive words and imposing a length range, there are 
# 	far too many zany personal names, obscure geographical locations, and extra-English words for it to be useful or fair to the player
# pivoting instead to a curated list of just hard hangman words found online

dict_list = open("wordlist.txt", 'r')
hangman_list = open("culled_wordlist.txt", 'w')


cur_line = dict_list.readline()
print(cur_line)

for line in dict_list:
	if "'" in line or len(line) < 7 or len(line) > 11:
		continue
	else:
		hangman_list.write(line)




dict_list.close()
hangman_list.close()

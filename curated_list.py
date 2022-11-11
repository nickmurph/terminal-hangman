# curated_wordlist.txt adopted from www.hangmanwords.com/words with slight modification
def return_curated_list():
	curated_file = open("word_lists/curated_wordlist.txt")
	curated_list = []

	for line in curated_file:
		curated_list.append(line[:-1])

	#print(curated_list)
	curated_file.close()
	return curated_list

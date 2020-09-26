def markov_tweet():
	#Created a nested dictionary with the 1st Key = a word second key = possible words that come after and value = counter
	words_dic = {}
	with open("prunedLyrics.txt", 'r', encoding="utf-8") as f:
		for line in f:
			line = line.replace("\n"," \n")
			words_list = line.split(" ")
			for index, word in enumerate(words_list):
				temp_kv_dic = {}
				#if we encounter a new line, move on to next line
				if word == "\n":
					break
				#check if a word exists in the dictionary, if not intialize with the {currentword: {the next word:1}}
				elif word not in words_dic:
					temp_kv_dic.update({words_list[index+1]:1})
					words_dic.update({word:temp_kv_dic})
				#if word is in dictionary, check if the following word is a key, if not intialize it, if it is update value
				elif word in words_dic:
					if words_list[index+1] in words_dic[word]:
						words_dic[word][words_list[index+1]] += 1
					else:
						temp_kv_dic.update({words_list[index+1]:1})
						words_dic[word].update(temp_kv_dic)
		
		print(words_dic)
				
#words_dic contains a dictionary with the following format
#{word:{nextword:appearances, anotherwordthatcomesafter:appearances}}
markov_tweet()


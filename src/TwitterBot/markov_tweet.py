def markov_tweet():
	#Created a nested dictionary with the 1st Key = a word second key = possible words that come after and value = counter
	words_dic = {}
	with open("prunedLyrics.txt", 'r', encoding="utf-8") as f:
		# while True:
		words = f.readline()
		words = words.replace("\n"," \n")
		words_list = list(words.split(" "))
		for index, word in enumerate(words_list):
			temp_key_value_dic = {}
			temp_value = 0
			if word == "\n":
				break
			if words_dic.get(word) == None:
				temp_key_value_dic.update({words_list[index+1]:1})
				words_dic.update({word:temp_key_value_dic})	
			#else: what happens when the dictionary already exists
			#must check if temp key is already there if it is updtae value
			#if temp key is not there create a new temp key with a value of 1
			print(words_dic)
markov_tweet()


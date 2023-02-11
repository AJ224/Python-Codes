def getDuplWords(s):
	#this dictionary will store word as key and its occurence in string as value
	d = dict()
	
	#separating words from sentence into word's list
	s = list(s.split(" "))

	#this set is used to remove 
	#duplication of words in original words string
	#resulting, reduction in loop iterations.
	s2 = set(s)


	#counting occurences of each word
	for word in s2:
		d[word] = s.count(word)

	lst = []
	#duplicated words
	for word in d.keys():
		if d[word] > 1:
			lst.append(word)

	return lst


if __name__ == '__main__':
	s = input()

	res = getDuplWords(s);

	print(res)
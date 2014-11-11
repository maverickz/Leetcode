from string import ascii_lowercase

def word_ladder(src, dst, word_list):
	if len(src) != len(dst):
		return []

	word_queue = []
	word_queue.append([src])
	char_list = list(ascii_lowercase)
	word_list.remove(src)

	while word_queue:
		path = word_queue.pop(0)
		last_word = path[-1]

		if last_word == dst:
			return path

		for i in xrange(len(last_word)):
			char_array = list(last_word)
			for char in char_list:
				char_array[i] = char 
				new_word = ''.join(char_array)

				if new_word in word_list:
					new_path = list(path)
					new_path.append(new_word)
					word_queue.append(new_path)
					# Remove word from word list to prevent loops
					# and to make sure the word is not processed
					# more than once
					word_list.remove(new_word)
	return []

if __name__ == '__main__':
	word_list = ["hit","hot","dot","dog","lot","log"]
	src = "hit"
	dst = "log"
	print word_ladder(src, dst, word_list)


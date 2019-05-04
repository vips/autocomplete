_end = '_end_'

def make_trie(words):
	"""
	Make trie for each word
	word = 'powerline'
	output will be
	{'p': {'o': {'w': {'e': {'r': {'l': {'i': {'n': {'e': {'_end_': '_end_'}}}}}}}}}}
	"""
	root = dict()
	for word in words:
		current_dict = root
		for letter in word:
			current_dict = current_dict.setdefault(letter, {})
		current_dict[_end] = _end
	return root

def in_trie(trie, word):
	"""
	check whether word exists in a trie
	"""
	current_dict = trie
	for letter in word:
		if letter in current_dict:
			current_dict = current_dict[letter]
		else:
			return False
	else:
		if _end in current_dict:
			return True
		else:
			return False

def traverse(selected_dict, prefix_word):
	"""
	traverse the sutree and return all possible result starting with prefix_word
	"""
	current_dict = selected_dict
	if current_dict:
		for letter in current_dict:
			if letter is _end:
				yield prefix_word
			else:
				yield from traverse(current_dict[letter], prefix_word+letter)

def prefix_lookup(trie, prefix_word):
	"""
	traverse the trie to reach out to the node represented by word and return the subtree
	e.g.
	
	trie (representing 'poqwerline') 
		{'p': {'o': {'w': {'e': {'r': {'l': {'i': {'n': {'e': {'_end_': '_end_'}}}}}}}}}}
	input_word  = 'powe'
	output:
		{'r': {'l': {'i': {'n': {'e': {'_end_': '_end_'}}}}}}
	"""
	current_dict = trie
	for letter in prefix_word:
		if letter in current_dict:
			current_dict = current_dict[letter]
		else:
			return {}
	else:
		return current_dict

def get_prefix_matched_result(trie, prefix_word):
	return [i for i in traverse(prefix_lookup(trie, prefix_word), prefix_word)]



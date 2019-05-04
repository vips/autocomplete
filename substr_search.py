from nltk import ngrams
from collections import defaultdict

def generate_ngram(word_list):
	"""
		generate all possible n-gram for each word
		e.g.
		word = 'powerline'
		Size of word is 9
		Generate 2-gram, 3-gram, 4-gram, 5-gram, 6-gram, 7-gram, 8-gram
		output = ['po', 'ow', 'we', 'er', 'rl', 'li', 'in', 'ne', 'pow', 'owe', 'wer', 'erl', 'rli', 'lin', 
			'ine', 'powe', 'ower', 'werl', 'erli', 'rlin', 'line', 'power', 'owerl', 'werli', 'erlin', 
			'rline', 'powerl', 'owerli', 'werlin', 'erline', 'powerli', 'owerlin', 'werline']
		
		Reverse index each n-gram to original word

	"""
	ngram_dict = defaultdict(list)
	for each_word in word_list:
		"ignore first word"
		word = each_word[1:]
		for l in range(2, len(word)-1):
			for ng in ngrams(word, l):
				ngram_dict[''.join(ng)].append(each_word)
	return ngram_dict


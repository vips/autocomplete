def load_data():
	words_freq = open('word_search.tsv', 'r').readlines()
	data = [tuple(each_line.split()) for each_line in words_freq]
	return dict([(w, int(f)) for w,f in data])

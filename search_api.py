from flask import Flask, request
import json
from word_search.prefix_search import make_trie, get_prefix_matched_result
from word_search.substr_search import generate_ngram
from word_search.data import load_data
from word_search.spell_corrector import correction


WORDS_FREQ = load_data()
final_trie = make_trie(WORDS_FREQ.keys())
ngram_index_data = generate_ngram(WORDS_FREQ.keys())


result_limit = 25

app = Flask(__name__)

@app.route("/search", methods=('GET',))
def search_api():
	global result_limit
	prefix_string 			=	request.args.get('word')
	ret_result 				=	[]
	"Add exact match to result"
	if prefix_string in WORDS_FREQ:
		ret_result.append(prefix_string)
	"Get list of prefix maches and sort based on the frequency"
	prefix_matched_result 	=	get_prefix_matched_result(final_trie, prefix_string)
	sorted(prefix_matched_result, key=WORDS_FREQ.get)
	ret_result.extend(prefix_matched_result[:(result_limit-len(ret_result))])
	if len(ret_result)>=result_limit:
		return json.dumps(ret_result)
	print (ret_result)
	"Get list of substring maches"
	substr_matched_result = ngram_index_data[prefix_string]
	sorted(substr_matched_result, key=WORDS_FREQ.get)
	ret_result.extend(substr_matched_result[:(result_limit-len(ret_result))])
	if len(ret_result)==0:
		"spell checker"
		return json.dumps(correction(prefix_string))
	return json.dumps(ret_result)

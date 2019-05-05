from flask import Flask, request
import time
import json
from prefix_search import make_trie, get_prefix_matched_result
from substr_search import generate_ngram
from data import load_data
from spell_corrector import correction


WORDS_FREQ = load_data()
final_trie = make_trie(WORDS_FREQ.keys())
ngram_index_data = generate_ngram(WORDS_FREQ.keys())


result_limit = 25

app = Flask(__name__)

@app.route("/search", methods=('GET',))
def search_api():
	start_time = time.time()*1000
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
		return json.dumps({'data': ret_result, 'time_taken': '%s milliseconds'%(time.time()*1000-start_time)})
	print (ret_result)
	"Get list of substring maches"
	substr_matched_result = ngram_index_data[prefix_string]
	sorted(substr_matched_result, key=WORDS_FREQ.get)
	ret_result.extend(substr_matched_result[:(result_limit-len(ret_result))])
	if len(ret_result)==0:
		"spell checker"
		return json.dumps({'data': [correction(prefix_string)], 'time_taken': '%s milliseconds'%(time.time()*1000-start_time)})
	return json.dumps({'data': ret_result, 'time_taken': '%s milliseconds'%(time.time()*1000-start_time)})



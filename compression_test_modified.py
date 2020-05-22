
from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords
import numpy as np
import networkx as nx
import sys

def read_article(file_name):
	file = open(file_name, "r")
	filedata = file.readlines()
	article = filedata[0].split(". ")
	sentences = []
	for sentence in article:
		#print('!!!',sentence
		sentences.append(sentence.replace("[^a-zA-Z]", ""))
		#sentences.pop() 
	
	return sentences


def sentence_similarity(sent1, sent2, stopwords=None):    
	if stopwords is None:        
		stopwords = []     
	sent1 = [w.lower() for w in sent1]    
	sent2 = [w.lower() for w in sent2]     
	all_words = list(set(sent1 + sent2))    
	vector1 = [0] * len(all_words)    
	vector2 = [0] * len(all_words)     
	# build the vector for the first sentence   
	for w in sent1:       
		if w in stopwords:            
			continue        
	vector1[all_words.index(w)] += 1     
	# build the vector for the second sentence    
	for w in sent2:        
		if w in stopwords:           
			continue        
	vector2[all_words.index(w)] += 1     
	return 1 - cosine_distance(vector1, vector2)

def remove_stopwords(sentences, stop_words):
	# Create an empty similarity matrix
	procesed = []
	for items in sentences:
		items = items.replace(',','')
		items = items.replace('"','')
		result = [word.lower() for word in items.split(' ') if word.lower() not in stop_words]
		#result = ' '.join(result)
		procesed.extend(result)

	return (procesed)

def getWeight(procesed):
	procesed.sort()
	unique = {}
	for items in procesed:
		if items in unique:
			unique[items]+=1
		else:
			unique[items] = 1

	big = 0

	for key,value in unique.items():
		if value>big:
			big = value

	for items in unique:
		unique[items] =  unique[items]/big

	return (unique)

def sumarise(sentences, weights):
	final = []
	for items in sentences:
		temp = items.split(' ')
		score =  0
		for words in temp:
			if words.lower() in weights:
				score+=weights[words.lower()]

		final.append((score, items))

	final =  (sorted(final, key=lambda x:x[0], reverse=True))

	for items in final:
		print(items[0],': ',items[1])








def generate_summary(file_name, top_n=5):
	stop_words = stopwords.words('english')
	stop_words+=['a','at','an']
	summarize_text = []
	# Step 1 - Read text and tokenize
	sentences =  read_article(file_name)
	# Step 2 - Generate Similary Martix across sentences
	procesed = remove_stopwords(sentences, stop_words)

	weights = getWeight(procesed)

	ordered = sumarise(sentences, weights)



	# Step 3 - Rank sentences in similarity martix
	# sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
	# scores = nx.pagerank(sentence_similarity_graph)
	# print (scores)
	# # Step 4 - Sort the rank and pick top sentences
	# ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
	# #print("Indexes of top ranked_sentence order are ", ranked_sentence)
	# for i in range(top_n):
	#   summarize_text.append(" ".join(ranked_sentence[i][1]))
	# # Step 5 - Offcourse, output the summarize texr
	# #print("Summarize Text: \n", ". ".join(summarize_text))

generate_summary('test.txt')
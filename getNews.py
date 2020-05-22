from fireBase_io import db
import sys
import json
import requests
import os
from requests.auth import HTTPBasicAuth
from newsapi import NewsApiClient
from newspaper import Article
import re


token = 'c6c56744857247b0a185ae62a5953cf2'
db_url = 'https://debunk-the-myths.firebaseio.com/'

filtering_key = ['india', 'covid', ]

class newsob:
	def __init__(self,id):
		self.url = None
		self.text = None
		self.imageurl = None
		self.title = None
		self.author = None
		self.id = id

	def viewArticle(self):
		print('')
		print ('Title: %s'%self.title)
		print ('Id is %s and length is %s characters'%(self.id,str(len(self.text))))
		print('')

	def formatArticletoDb(self):
		out = {self.id:[{'title':self.title},{'author':self.author}, {'content':self.text},{'url': self.url}, {'imageurl':self.imageurl}]}
		return(out)



def get_full_text(url):
	try:

		article = Article(url)
		article.download()
		article.parse()
		return(article.text)
	except Exception as e:
		print (e)
		#return 'FAIL'
def getNewsId(items):
	newsid = items['source']['name'] + '_'  +items['publishedAt']
	newsid = newsid.replace(':','_')
	newsid = newsid.replace('.com','')
	newsid = newsid.replace('.','')
	return newsid


newsapi = NewsApiClient(api_key=token)


## Initial query to get bunch of articles, urls'e etc (step 1) from newapi.org

## To do - filter query based on sources
all_articles = newsapi.get_everything(q='covid india',
                                      from_param='2020-05-15',
                                      sources='bbc-news,cbc-bews,cnn,fox-nees,google-news-in,the-times-of-india,the-hindu',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)


articleCollection = []

if all_articles['status']=="ok":
	for items in all_articles["articles"]:

		newsid = getNewsId(items)
		
		news = newsob(newsid)
		news.url = items['url']
		news.imageurl = items['urlToImage']
		news.title = items['title']
		news.author = items['author']

		print('Trying for %s'%newsid)

		## get ful contnet for an article using url using 'newspaper' python module
		full_text = get_full_text(news.url)
		if full_text==None:
			continue

		## filtering logic using keywords
		fail = 0
		for words in filtering_key:
			if re.search(words, full_text, re.IGNORECASE):
				continue
			else:
				fail = 1
				break


		if full_text !=None and fail!=1:
			news.text = full_text
			articleCollection.append(news)
		else:
			continue




mydb = db('https://debunk-the-myths.firebaseio.com/')

print(len(articleCollection))

for items in articleCollection:
	print('!!!!')
	items.viewArticle()
	#mydb.write('/test/articles',items.formatArticletoDb())
	out = items.formatArticletoDb()

	result = mydb.write('/test/articles',out)
	print (result)







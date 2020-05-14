from fireBase_io import db
import sys
import json
import requests
import os
from requests.auth import HTTPBasicAuth
from newsapi import NewsApiClient
from newspaper import Article


token = 'c6c56744857247b0a185ae62a5953cf2'
db_url = 'https://debunk-the-myths.firebaseio.com/'

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

all_articles = newsapi.get_everything(q='covid india',
                                      from_param='2020-05-10',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

#print(json.dumps(all_articles, indent=2))



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

		full_text = get_full_text(news.url)
		if full_text !=None:
			news.text = full_text
			articleCollection.append(news)
		else:
			continue



mydb = db('https://debunk-the-myths.firebaseio.com/')

for items in articleCollection:
	items.viewArticle()
	#mydb.write('/test/articles',items.formatArticletoDb())
	out = items.formatArticletoDb()
	print(out)
	print(type(out))

	result = mydb.write('/test/articles',out)







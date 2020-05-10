import sys
import json
import requests
import os
from requests.auth import HTTPBasicAuth


token = 'c6c56744857247b0a185ae62a5953cf2'


def get_url(query,token):
	if  ' ' in query:
		query = query.replace(' ','%20')
	return("http://newsapi.org/v2/everything?q=%s&apiKey=%s" % (query, token))

def send_api(url,token):

	headers = {'X-auth-token' : token}

	try:
		response = requests.get(url=url, headers=headers, verify=False)
		return(response.json())
	except Exception as e:
		print(e)

url = get_url('covid-19 India', token)
result = send_api(url, token)

#result = json.dumps(result, indent=4)

with open ('news.json','a') as fh:
	fh.write(json.dumps(result, indent=4))

print ('Done!')





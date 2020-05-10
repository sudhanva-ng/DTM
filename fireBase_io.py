from firebase import firebase  
import json
import sys


class db:
	def __init__(self, url):
		self.handler = firebase.FirebaseApplication(url, None)

	def write(self,dest,data):
		result = self.handler.post(dest,data)
		return result


	def read(self,dest,obj):
		result = self.handler.get(dest, obj)
		return (result)

# mydb = db('https://debunk-the-myths.firebaseio.com/')
# result = mydb.read('/test/-M6GZph798ThetACfTBN/Members/1/','Name')

# data = {'Members':[{'Name':'Sudhanva','cec':'sudng'},{'Name':'Nikitha','cec':'ninagell'}]}
# result = mydb.write('/test/test1',data)

# print(result)


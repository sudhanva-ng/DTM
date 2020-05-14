from firebase import firebase  
import json
import sys


class db:
	def __init__(self, url):
		self.handler = firebase.FirebaseApplication(url, None)

	def write(self,dest,data):
		result = self.handler.patch(dest,data)
		return result


	def read(self,dest,obj):
		result = self.handler.get(dest, obj)
		return (result)

# mydb = db('https://debunk-the-myths.firebaseio.com/')
# # result = mydb.read('/test/-M6GZph798ThetACfTBN/Members/1/','Name')

# # data = {'Members':['Name':'Sudhanva','cec':'sudng'},{'Name':'Nikitha','cec':'ninagell'}]}

# #data = {'https://ichef.sudng s :s:':['Name','https://ichef.sudng s :s:','test']}

# data = {'Bbc-com_2020-05-11T23_00_15Z': ['Safoora Zargar: Why did India jail a pregnant student during Covid-19?', 'https://www.bbc.com/news/world-asia-india-52608589', 'https://ichef.bbci.co.uk/news/1024/branded_news/14066/production/_112222028_photo-2020-05-04-12-17-38.jpg']}
# # print(type(data))

# result = mydb.write('/test/test1',data)

# print(result)


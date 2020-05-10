from firebase import firebase  
import json

firebase = firebase.FirebaseApplication('https://debunk-the-myths.firebaseio.com/', None)  

data = {'Members':[{'Name':'Sudhanva','cec':'sudng'},{'Name':'Nikitha','cec':'ninagell'}]}

#print(json.dumps(data, indent=4))

# data = 

# 		 { 
# 		  'Name': 'Sudhanva',  
#           'id': 1,  
#           'cec': 'sudng' 
#           }  


# # Write to databse

# result = firebase.post('/test/',data)
# print(result)

# #Read from databse 
result = firebase.get('/test/-M6GZph798ThetACfTBN/Members/1/','Name')

print(type(result))

print(result) 
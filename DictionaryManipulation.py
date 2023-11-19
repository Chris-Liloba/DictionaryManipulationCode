"""
Created on Sun Nov 19 17:11:54 2023

@author: linyuluc
"""
#These are examples of Dictionary Codes and their manipulation 
dictionary_Liloba = {
  "name": "Chris",
  "nickname": "Liloba",
  "nationality": "Kenyan"
}


#print("------------This is Code Snippet number 2-----------")

dictionary_Liloba['age'] = 24

print(dictionary_Liloba) # {'nationality': 'Brazilian', 'age': 24, 'nickname': 'Tk', 'name': 'Leandro'}

dictionary_Liloba = {
  "name": "Chris",
  "nickname": "Liloba",
  "nationality": "Kenyan",
  "age": 24
}


#getting the key and value in a dictionary
for key, value in dictionary_Liloba.items():
    print("My %s is %s" %(attribute, value))
    

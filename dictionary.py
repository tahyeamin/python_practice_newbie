dictionary= {

"brand": "ford",
"model ": "Mustand",
"model " : "Expedition",  #Duplicate values will overwrite existing values
"year": 1976


}

print(dictionary)

print(dictionary["brand"])  #accessing value without using get function

print(dictionary["model "]) #string should be same, Accessing value using key 



print(dictionary.get("year")) #accessing value using get function

print(len(dictionary))

print(type(dictionary))

k = dictionary.keys()

print(k)

print(dictionary)



flist = ["practicing", "Python", "list"]
print(flist)



# A color normal List

list = ["red","green", "yellow", "black"]
print(list)



# Add an item to the end of the list

list.append("blue")
print(list)



# Insert an item at a given position (index 1 & 3)

list.insert(1,"white")
print(list)

list.insert(3, "white")
print(list)



#  Modify an element by using the index of the element

list[3]="skyblue"
print(list)


# Remove an item from the list

list.remove("blue")
list.remove("black")
print(list)




#Remove all items from the list

list.clear()
print(list)




# Create another list

list1= ['red', 'white', 'green', 'yellow', 'black', 'blue']
print(list1)



# Cut first two items from a list:

print(list1[0:2])


# Cut some item from a list:

print(list1[1:2])
print(list1[3:4])
print(list1[1:3])
print(list1[3:-1]) #using negative indexing
print(list1[:2])



# Creates copy of original list:

print(list1[:])



# Remove the item at the given position in the list

list1.pop(2)
print(list1)
list1.pop(3)






#create another list

list2 = ['red', 'white', 'green', 'yellow', 'black', 'blue']
print(list2)

'''
# Return the index in the list

list2.index("red")
print(list2)
list

'''

color_list=["Red", "Blue", "Green", "Black"]
print(color_list)

color_list=["Red", "Blue", "Green", "Black", "Blue"]
print(color_list)

color_list.count("Blue")



#Return the number of times 'x' appear in the list

list2.append("white")
print(list2)
list2.count("white")
print(list2)
















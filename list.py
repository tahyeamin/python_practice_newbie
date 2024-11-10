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

list2 = ['red', 'white', 'green', 'yellow', 'black', 'blue', 'white']
print(list2)


# Return the index in the list, SP

print(list2.index("red"))
print(list2.index("black"))
print(list2.index("white",1,6))




#Return the number of times 'x' appear in the list

print(list2.count("white"))
print(list2.count("green"))



#Sort the items of the list in place

list2.sort(reverse=True)
print(list2)
print(sorted(list2))


#Reverse the elements of the list in place
#creating another list


list3 =['red', 'white', 'green', 'yellow', 'black', 'blue', 'white']

print("reversing this list :",list3)
list3.reverse()
print(list3)



#Return a shallow copy of the list


print(list3)
print(list3.copy())


#Convert a list to a tuple in Python

tuple1 = tuple(list3)
print(tuple1)



#How to use the double colon [ : : ]?

newlist = list3 [1:6:2] #list[start,stop,step] step for increament
print(newlist)

newlist = list3[::2]
print(newlist)

newlist = list3[6:0:-2]
print(newlist)



#Find the largest and the smallest item in a list

list4= [1,2,3,4,5,6,7,10,20]
print(max(list4))
print(min(list4))


#Compare two lists in Python


list5 = ["red", "white", "green", "yellow"]
list6 = ["red", "green", "white", "yellow"]

print(list5 == list6)

print(list5.sort() == list6.sort())




#Using Lists as Stacks

stacklist = ['black', 'blue', 'green', 'red']


print("declared stack list ", "\n", stacklist)
 
stacklist.append("white")
stacklist.append("yellow")

print("Stacks after pushing :" , stacklist)

stacklist.pop()
stacklist.pop()
stacklist.pop()

print("stack list after pop :", stacklist)



#Using Lists as Queues

from collections import deque

queuelist = deque(['black', 'blue', 'green', 'red'])


print("declared queue list ", "\n", queuelist)
 
stacklist.append("white")
stacklist.append("yellow")
print(queuelist)




















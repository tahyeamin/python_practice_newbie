single_value = ("black",)
print(single_value)


#create an empty tuple
empty_tuple =()
print (empty_tuple)


#create a tuple with different data types

tuplex =("strint", 1, True, 5.67)
print(tuple)


#create a tuple with numbers, notation without parenthesis

tuple_without_pt = 1, 2,3,4, "strint"
print(tuple_without_pt)


#get item (4th element and also from last)of the tuple by index


tuple1 = ('a', "b", "c",1,2,3,4)
print(tuple1[3])
print(tuple1[-4])

#How to know if an element exists within a tuple in Python?

print("a" in tuple1)
print(2 in tuple1)
print(40 in tuple1)


#list to tuple 

list2 = [5, 10, 7, 4, 15, 3]

tuple_2 = tuple(list2)

print(tuple_2)




#Unpack a tuple in several variables

tuple3 = 4,5,6,
print("before assign to variable :" , tuple3)

a, b, c = tuple3

print(a,b,c)
print(a+b+c)


#Add item in Python tuple!

tuple4 = 1,2,3,4,5,6
print(tuple4)


tuple4 = tuple4 +(7,8,)
print(tuple4)

tuple4 = tuple4[:5] +(9,10,)+ tuple4[5:]
print(tuple4)


#tuple to list 

list1 = list(tuple4)
print(list1)

#add item on list
list1.append(50)
print(list1)


#tuple count

tuple5 = (3,6,4,5,6,7,8,3)

count= tuple5.count(3)
print(count)




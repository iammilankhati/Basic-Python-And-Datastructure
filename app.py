
name = "namessssssss"
"""
# syntax
comments
variables
data types
numbers
Casting
strings
boolean
if else
for
while
advanced types
functions
class inheritance

"""


thislist = ["apple",'banana','cheery',"cherry"]

#general
print(thislist)
print(thislist[3])

print(len(thislist))

list2 = [1,2,4,5,65,6]
list3 = [True, False, False, False, False, False]


random_list  =["apple", 1, False]


print(type(random_list))


list3 = list(("apple","ball",'cat'))
print(type(list3))

# list Accessing

print(thislist[1])
print(thislist[-1])

thislist2 = ['apple','banana','cherry','oranage','kiwi','mango']
print(thislist2[2:])
print(thislist2[-3:])
print(thislist2[:3])

# check in list
if "grape" in thislist2:
    print(f'yes kiwi exist in the list')


# changing the list 
thislist3 = ['apple','banana','cherry','oranage']
thislist3[2] = "cabbage"

print(thislist3)

thislist3[1:3] = ["mango",'banana','cherry','oranage']
print(thislist3)


# Adding the items (append,insert,extend)
thislist4 = ['apple','banana','cherry','oranage']
# thislist4.append(["mango",'banana','cherry','oranage'])
print(thislist4)

thislist4.insert(1,'rice')
print(thislist4)

thislist4.extend(thislist2)
print(thislist4)

#remove the items(remove, pop,del,clear)
thislist5 = ['apple','banana','cherry','oranage','oranage']
thislist5.remove('banana')
print(thislist5)

thislist5.pop()
print(thislist5)

del thislist5[0]
print(thislist5)
thislist5.clear()

print(thislist5)


#looping in list
thislist6 = ['apple','banana','cherry','oranage']

#for loop
# for item in thislist6:
#     print(item)

#list comprehension
# [print(x) for x in thislist6]

#using range

# for i in range(0,len(thislist6)):
#     print(thislist6[i])


# i = 0
# while i < len(thislist6):
#     print(thislist6[i])
#     i += 1

# user_input = int(input('Please enter your age'))

# if user_input >= 18:
#     print(f'You can cast vote')
# elif user_input >= 13:
#     print(f'your age: {user_input} is under 18')
# else:
#     print('testing')



#sort(reverse=True)

thislist7 = [1,3,5,6,3,6,5]
thislist7.sort(reverse=True)
# thislist7.revers()
print(thislist7)

#join
list5 = thislist7 + thislist2

print(list5)

#copy
list10 = thislist3.copy()



























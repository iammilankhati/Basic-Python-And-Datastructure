""" List, tuple, set, dictionary """

# list
fruits = ['apple', 'mango', 'banana']

#accessing
print(fruits[0])
for fruit in fruits:
    print(fruit)
if 'apple' in fruits:
    print('yes')

#changing
fruits[0] = 'orange'
fruits.insert(0, 'orange')
fruits.append('watermilan')
fruits.extend(['coconut', 'graphes'])

# remove
fruits.pop(1)
fruits.remove('orange')
fruits.clear()
del fruits
fruits = ['apple', 'mango', 'banana']
# list comprehension
[print(x) for x in fruits if x.startswith('o')]

# list sorting
print(fruits.sort(reverse=True))
print(fruits.sort(key=str.lower))
fruits.reverse()

#tuples

subjects = ('maths', 'english', 'datastructure', 'ai', 'software development')

#looping tuple
print(subjects[1])
for sub in subjects:
    print(sub)

#update tuples
new_subjects = list(subjects)
new_subjects[1] = 'agile methodology'
subjects = tuple(new_subjects)

# similary we can use append, insert, extend, find, count

#unpack tuple
(sub1, sub2, *other) = subjects

#sets
subjects = {'maths', 'english', 'english', 'english'}
fruits = ['apple', 'mango', 'mango', 'mango', 'mango', 'banana']

# same as list and tuple but can't keep duplcates

print(subjects)
fruits = set(fruits)
subjects.add('newsubject')
subjects.update({
    'drawing',
    'physics',
})

subjects.discard('physics')
subjects.clear()

#dictionaries

student_info = {
    "name": "Milan Khati",
    "age": 24,
    'behaviour': "humble",
    'favorites': {
        'color': "black",
        'animal': 'deer',
        "hobby": 'problem solving',
    },
}

#accessing
# Call the lambda function and print the result

print(student_info.get('favorites'))

for keys in student_info.keys():
    print(keys)

for values in student_info.values():
    print(values)

for key, values in student_info.items():
    print(key, values)

""" calulator """


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
user_input = input('Enter the numbers and operator ? ')  # input as + 5 4
operator, operand1, operand2 = user_input.split()

result = operations[operator](int(operand1), int(operand2))
print(result)  # 9

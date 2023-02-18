## Python and Datastructures

## Basic

1. string
2. number
3. boolean
4. casting

## String Manipulation

1. indexing, slicing, modifying and commonly used methods

## Looping and Branching

1. if else
2. for loop, while

## Data Structures

1. List- _ordered and changeable,Allows duplicate._
   >list accessing
   >list modifying
   >list deletion
   >list comprehension
   >list sorting




2. Tuple - _ordered, unchangeable, Allows duplicates_
   >tuple accessing

    *casting types to list for update*   

3. Set -_unordered, unchangeable, unindexed, No duplicate_
   >most common use is remove the duplcates by casting

4. Dictionary - _ordered, changeable, No duplicate_
   >accessing
   >looping
#### Creating a calculator
```
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

```
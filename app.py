""" 


syntax
comments
variables
data types (basic, advanced)
casting(str, int)
operator

advanced data types(list,tuple,set dictionary)
loops: while, for loop
if else



"""


# functions


def add_number(first_number, second_number):
    result = first_number + second_number
    return result
    


print(add_number(5,3))





def show_name(name):




    print(f'My name is {name}')


show_name('Aryan')
show_name('prabin')


#args || parameters

#numbers of parameters
#*args (arbitary args)
def sum_num(*args):
    print(args[2:4])
    

sum_num(1,2,5,4,2)

#keyword arguments
def show_info(a,b,c):


    print(f'the smallest number is : {a}')


# show_info(a=6,b=5,c=9,d=5)


def show_all(**nums):
    print(f'His First name is :{nums["lname"]}')

show_all(fname="Aryan", lname="Ghimire")

#how to make funtions
#parameter ::   
   #*args
   #**keyargs
   #default:



def print_country(country="england"):
    print(f'I am from :{country}')

print_country("Nepal")


def function_food(food):
    #logic

    for x in food:
        print(x)
    
food = ['rice','orange','curry']

function_food(food)



def find_value(x):
    return x * 10

print(find_value(5))



#function (def,fn_name, return)
#args: 3 (*args, **kwargs, default)













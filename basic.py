""" Datatypes """

greet = "Hello, Welcome to Nepal!"  #string #immutable
age = 24  #int
height = 5.9  #float
is_active = True  #boolean
print(6 > 4)
list_ex = ['design', 'frontend', 'backend']  #list
tuple_ex = ('design', 'frontend', 'backend')  #tuple
set_ex = {'design', 'frontend', 'backend'}  #tuple
dict_ex = {
    "name": "Milan Khati",
    "age": '24',
    'fav': {
        "fruit": 'apple',
        "color": "black"
    },
}
""" Taking inputs """

# typecast: str(), int(), float()
name = input('Please enter your name ? ')
age = int(input('Please Enter you age'))  # type casting to int
""" String manipulation """
# strings are arrays

# slicing
username = "milan.khati@gmail.com"
print(username[3:6])
print(username[:6])
print(username[3:])

# modifying

username.upper()
username.strip()  # removes the white spaces
username.replace('m', '')
username.split('.')  #splits from . and returns array

print(f'Hello, {username}, How are you ? ')

# commonly used methods for strings

username.count('m')
username.indexOf('m')
username.lastIndexOf('m')
username.endswith('m')
username.find('m')
""" commonly used operators """
# ==  !=  >  >=  <  <=  is  is not  in  not in
# **, >> <<, |, not, and , or
print(5 == 6)
print(5 != 6)

if (username or username):  # and , not, is, is not,  in,
    print(username)

x = 6
y = 20

if (x & y):  # |, ^, ~, << >>
    pass
""" Looping and Branching """

age = 24
# ifelse
if (age >= 24):
    print('You can cast a vote.')
else:
    print('You can\'t cast a vote')

# for
for i in range(len(username)):
    print(username[i])
    
#while 
count = 5
while(count>0 ):
    print(count)
    count-+1
    
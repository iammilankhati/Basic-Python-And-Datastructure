

cars = ['range rover','lamborghini','suzuki']

for  car in cars:
    if car == 'lamborghini':
        break
    print(car)

user_input = int(input('Please enter n to exit ?'))

while user_input != 5:

    print(f'Welcome to homepage... {user_input}')
    user_input = input('Please enter n to exit ?')



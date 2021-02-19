while True:
    print('Enter your age: ')
    age = input()
    print(type(age))
    if age.isdecimal():
        break
    print('Please enter a some number your age')
while True:
    print('Select a new password(leter and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers. ')        
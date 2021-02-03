print('###### Welcome to Login Page #####')
User = 'SujahathMSM'          # Assigning a d Username
Pwd = 'Sujahath@Day_03_01'    # Assigning a Password
count=3
while True:
    Username = input('Enter the username: ')    # To get the username from user

    Password = input('Enter the password: ')    # To get the password from the user

    # checking the username and password

    if Username==User and Password==Pwd:
        print('*** Successful login *** ')
        break

    elif Username!=User and Password==Pwd:
        print('!!! Invalid Username !!!')

    elif Username==User and Password!=Pwd:
        print('!!! Invalid Password !!!')
    # Allowing user to significant number of login attempts
    else:
        print('Invalid Username and Password')
        count-=1
        print('!!!!Warning!!!!\nYou have',count,'login attempt(s) left')

    # If user fails to login within three attempts
    if count==0:
        print('>>>No more attempts left<<<')
        break

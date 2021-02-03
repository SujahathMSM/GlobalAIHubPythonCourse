login = {'Username':'SujahathMSM','Password':'Sujahath@Day_03_02'}   # # Assigning a d Username and a Password
print('***** Welcome to LOGIN page *****')
count=3
while True:
    Username = input('Enter the username: ')     # To get the username from user

    Password = input('Enter the password: ')     # To get the password from the user

    # checking the username and password

    if Username == login['Username'] and Password == login['Password']:
        print('*** Login Successful ***')
        break

    elif Username != login['Username'] and Password == login['Password']:
        print('!!! Invalid username !!!')

    elif Username == login['Username'] and Password != login['Password']:
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

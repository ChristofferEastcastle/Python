
def checkForLogin():
    choice = input("write l then enter if login, r then enter if register: ")
    if choice == 'l':
        login()
    elif choice == 'r':
        register()
    else:
        print('You did not put l or r, please try again')
        checkForLogin()

def checkIfUserExists(input, type):
    database = open("credentials.txt", "r")
    for line in database:
        dict = eval(line)
        if input == dict[f'{type}']:
            print(f"{type} is taken! Please try again!")
            return True

def register():
    print("Register")
    username = input("Username: ")
    while True:
        if checkIfUserExists(username, f'Username') == True:
            username = input("Username: ")
        else:
            break
    password = input("Password: ")
    while True:
        if checkIfUserExists(password, f'Password') == True:
            password = input("Password: ")
        else:
            break
    email = input('Email: ')
    while True:
        if checkIfUserExists(email, f'Email') == True:
            email = input('Email: ')
        else:
            break
    phonenumber = int(input('Phonenumber: '))
    while True:
        if checkIfUserExists(phonenumber, f'Phonenumber') == True:
            phonenumber = int(input('Phonenumber: '))
        else:
            break
    confirm = input('Confirm your password by entering it again: ')
    if len(username) > 0 and len(password) > 0:
        while True:
            if password != confirm:
                print('Confirm password is wrong! Please try again')
                confirm = input('Confirm your password by entering it again: ')
            else:
                break
        writeToFile(username, password, email, phonenumber)
        print('Account has been created!')


def login():
    print("Log-in")
    username = input('Username: ')
    password = input('Password: ')
    credentials = open("credentials.txt", "r")
    correct = False
    for line in credentials:
        if username in line and password in line:
            correct = True
            print('Username and password ok')
            yesNo = input('Would you like to see your account? yes/no ')
            if yesNo == 'yes':
                print(line)
                while True:
                    changes = input("Do you want to make any changes? yes/no ")
                    if changes == "yes":
                        makeChanges(line)
                    else:
                        print('This session has been terminated.')
                        return
            else:
                print('This session has been terminated.')
                return
        elif username not in line and password not in line:
            correct = False
    if correct == False:
        print('Username or password not ok')


def writeToFile(username, password, email, phonenumber):
    user = {"Username": username, "Password": password, "Email": email, "Phonenumber": phonenumber}
    doc = open('credentials.txt', 'a')
    doc.write(f'\n{user}')

def makeChanges(line):
    dict = eval(line)
    print(dict)
    change = input(f'What would you like to change? ')
    dict[f'{change}'] = input("What do you want to change it to? ")
    credentials = open("credentials.txt", 'r')
    for lines in credentials:
        if lines == line:
            print(lines, dict)
            lines = lines.replace(lines, f'{dict}')
            credentials = open('credentials.txt', "a")
            credentials.write(lines)


checkForLogin()
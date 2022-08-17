import json
import os
import random
import argparse
import sys

from termcolor import colored

# TODO: Add params to run directly from command line
# TODO: Add GUI
# TODO: Add update and delete functionality
# TODO: Store multiple creds of same app in same object
# TODO: search functionality

version = '1.2-alpha'
usingarguments = False
if len(sys.argv) != 1:
    usingarguments = True


def start():
    print('\nWelcome to pa55G3n V' + str(version))
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("data/passwords.json"):
        with open('data/passwords.json', 'w') as passFile:
            passFile.write('[]')
            passFile.close()
    elif os.stat('data/passwords.json').st_size == 0:
        with open('data/passwords.json', 'w') as passFile:
            passFile.write('[]')
            passFile.close()
    choose()


def choose():
    print('\n1. Generate a password')
    print('2. View saved passwords')
    print('3. GUI')
    print('4. Exit')
    choice = input('\nEnter your choice: ')
    if choice == '1':
        passComplexity()
    elif choice == '2':
        showPasswords()
    elif choice == '3':
        # gui.start()
        print(colored('\nComing soon!', 'red'))
        choose()
    elif choice == '4':
        print('Thank you for using pa55G3n, goodbye!')
        exit(0)
    else:
        print(colored('\nInvalid choice', 'red'))
        choose()


def showPasswords():
    try:
        with open('data/passwords.json', 'r') as passFile:
            emptyArray = True if json.load(passFile) == [] else False
        if os.stat('data/passwords.json').st_size == 0 or emptyArray:
            print(colored('\nNo saved passwords.', 'yellow'))
        elif os.stat('data/passwords.json').st_size > 0:
            with open('data/passwords.json', 'r') as passFile:
                saved = json.load(passFile)
                passFile.close()
            print('\nSaved passwords:\n', saved)
        choose()
    except FileNotFoundError:
        print(colored('\nCould not find the passwords file.', 'red'))
        choose()


def passComplexity():
    print('\n1. Simple', colored('(Lowercase characters only)', 'yellow'), colored('[NOT RECOMMENDED]', 'red'))
    print('2. Medium', colored('(Lowercase and uppercase characters)', 'yellow'))
    print('3. Hard', colored('  (Lowercase, uppercase and numbers)', 'yellow'))
    print('4. Secure', colored('(Lowercase, uppercase, numbers and special characters)', 'yellow'),
          colored('[RECOMMENDED]', 'green'))
    print('5. Exit')
    complexity = input('\nEnter your choice: ')
    if complexity in ('1', '2', '3', '4'):
        passLength(complexity)
    elif complexity == '5':
        print('Thank you for using pa55G3n, goodbye!')
        exit(0)
    else:
        print(colored('\nInvalid choice', 'red'))
        passComplexity()


def passLength(complexity):
    print('\nHow long should the password be?\nThe default length is 8 characters.')
    length = input('\nEnter the desired length: ')
    if length == '':
        generate(complexity, 8)
    elif int(length) > 0:
        generate(complexity, length)
    else:
        print(colored('\nInvalid choice', 'red'))
        print(length, type(length))
        passLength(complexity)


def savePassword(password):
    try:
        app, username = '', ''
        while app == '':
            app = input('\nEnter the website/app name for which you are using this password: ')
        while username == '':
            username = input('\nEnter the username/email associated with this account: ')
        with open('data/passwords.json', 'r') as passFile:
            credentials = json.load(passFile)
        credentials.append({app: {"username": username, "password": password}})
        with open('data/passwords.json', 'w') as passFile:
            json.dump(credentials, passFile, indent=4)
            passFile.close()
        print(colored('\nPassword saved!', 'green'))
        choose()
    except:
        print(colored('\nError, could not save the password.', 'red'))
        choose()


def whatNext(password):
    save = input('\nDo you want to save this password? (Y/n): ')
    if save.lower() == 'y' or save.lower() == '':
        savePassword(password)
    elif save.lower() == 'n':
        passComplexity()


def generate(choice, length):
    complexity = 'simple'
    password = ''
    intLength = int(length)
    charsSimple = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    charsMedium = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    charsHard = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                 '8', '9']
    charsSecure = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']',
                   '|', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/', '\\', '~', '`']
    for i in range(intLength):
        password = password + random.choice(charsSimple)
    if choice == '2':
        complexity = 'medium'
        for i in range(intLength):
            password = password + random.choice(charsMedium)
    elif choice == '3':
        complexity = 'hard'
        for i in range(intLength):
            password = password + random.choice(charsHard)
    elif choice == '4':
        complexity = 'secure'
        for i in range(intLength):
            password = password + random.choice(charsSecure)
    print(colored('Generated ' + complexity + ' password : ' + password, 'green'))
    if not usingarguments:
        whatNext(password)
        choose()
    else:
        savePassword(password)


# savePassword(generate(str(4), 8))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pa55G3n ' + version + ' - A simple password Generator')
    parser.add_argument('--version', action='version', version='%(prog)s ' + version)
    parser.add_argument('-g', '--generate', action='store_true', help='generate a password')
    parser.add_argument('-v', '--View', action='store_true', help='view saved passwords')
    parser.add_argument('-u', '--gui', action='store_true', help='start in GUI mode [AVAILABLE IN NEXT VERSION]')
    parser.add_argument('-c', '--complexity', type=str, default='4', help='choose password complexity',
                        choices=['1', '2', '3', '4'])
    parser.add_argument('-l', '--length', type=int, default='8', help='choose password length')
    parser.add_argument('-s', '--save', action='store_true', help='auto save on generation')
    args = parser.parse_args()
    if not usingarguments:
        start()
    else:
        if args.gui:
            # gui.startGUI()
            print((colored('\nAvailable soon...', 'red')))
            exit(0)
        elif args.View:
            showPasswords()
        elif args.generate and args.complexity and args.length and args.save:
            savePassword(generate(str(args.complexity), args.length))
        elif args.generate and args.complexity and args.length:
            generate(str(args.complexity), args.length)
        elif args.generate:
            passComplexity()
        else:
            print(colored('\nError, invalid argument.', 'red'))
            exit(1)

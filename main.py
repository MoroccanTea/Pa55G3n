import json
import os
import codecs
import tkinter as tk
from PIL import Image, ImageTk
import random
from termcolor import colored

# TODO: Add params to run directly from command line
# TODO: Add GUI
# TODO: Add update and delete functionality
# TODO: Store multiple creds of same app in same object

version = '1.0-alpha'


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
    print('3. Exit')
    choice = input('\nEnter your choice: ')
    if choice == '1':
        passDifficulty()
    elif choice == '2':
        showPasswords()
    elif choice == '3':
        print('Thank you for using pa55G3n, goodbye!')
        exit(0)
    else:
        print(colored('\nInvalid choice', 'red'))
        choose()


def showPasswords():
    try:
        if os.stat('data/passwords.json').st_size == 0:
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


def passDifficulty():
    print('\n1. Simple', colored('(Lowercase characters only)', 'yellow'), colored('[NOT RECOMMENDED]', 'red'))
    print('2. Medium', colored('(Lowercase and uppercase characters)', 'yellow'))
    print('3. Hard', colored('  (Lowercase, uppercase and numbers)', 'yellow'))
    print('4. Secure', colored('(Lowercase, uppercase, numbers and special characters)', 'yellow'),
          colored('[RECOMMENDED]', 'green'))
    print('5. Exit')
    choice = input('\nEnter your choice: ')
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
        passLength(choice)
    elif choice == '5':
        print('Thank you for using pa55G3n, goodbye!')
        exit(0)
    else:
        print(colored('\nInvalid choice', 'red'))
        passDifficulty()


def passLength(choice):
    print('\nHow long should the password be?\nThe default length is 8 characters.')
    length = input('\nEnter the desired length: ')
    if length == '':
        generate(choice, 8)
    elif int(length) > 0:
        generate(choice, length)
    else:
        print(colored('\nInvalid choice', 'red'))
        print(length, type(length))
        passLength(choice)


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
        choose()


def generate(choice, length):
    difficulty = 'simple'
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
        difficulty = 'medium'
        for i in range(intLength):
            password = password + random.choice(charsMedium)
    elif choice == '3':
        difficulty = 'hard'
        for i in range(intLength):
            password = password + random.choice(charsHard)
    elif choice == '4':
        difficulty = 'secure'
        for i in range(intLength):
            password = password + random.choice(charsSecure)
    print(colored('Generated ' + difficulty + ' password : ' + password, 'green'))
    whatNext(password)
    choose()


if __name__ == '__main__':
    start()
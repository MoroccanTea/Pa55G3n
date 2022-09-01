import json
import os
import random
import argparse
import sys
import string
from termcolor import colored

# TODO: 1. Add update and delete functionality (WIP)
# TODO: 2. Encrypt passwords using master password
# TODO: 3. Add 2FA
# TODO: 4. Add database connectivity (SQLite, MySQL & MongoDB)
# TODO: 5. Add security measures (e.g. prevent buffer overflow attacks, canary, etc.)
# TODO: 6. Add GUI
# TODO: 7. Add browser extension


version = '1.3-alpha'
using_arguments = False
if len(sys.argv) != 1:
    using_arguments = True


def start():
    print('\nWelcome to pa55G3n V' + str(version))
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("data/credentials.json") or os.stat('data/credentials.json').st_size == 0:
        with open('data/credentials.json', 'w') as credsFile:
            credsFile.write('{}')
            credsFile.close()
    choose()


def choose():
    print('\n1. Generate a password')
    print('2. View all saved passwords')
    print('3. GUI')
    print('4. Search specific password')
    print('5. Update existing credentials')
    print('6. Delete existing credentials')
    print('7. Exit')
    choice = input('\nEnter your choice: ')
    if choice == '1':
        pass_complexity()
    elif choice == '2':
        show_passwords()
    elif choice == '3':
        # gui.start()
        print(colored('\nComing soon!', 'red'))
        choose()
    elif choice == '4':
        search(None)
    elif choice == '5':
        update()
    elif choice == '6':
        delete()
    elif choice == '7':
        print('Thank you for using pa55G3n, goodbye!')
        exit(0)
    else:
        print(colored('\nInvalid choice', 'red'))
        choose()


def show_passwords():
    try:
        with open('data/credentials.json', 'r') as passFile:
            empty_array = True if json.load(passFile) == [] else False
        if os.stat('data/credentials.json').st_size == 0 or empty_array:
            print(colored('\nNo saved passwords.', 'yellow'))
        elif os.stat('data/credentials.json').st_size > 0:
            with open('data/credentials.json', 'r') as passFile:
                saved = json.load(passFile)
                passFile.close()
            print('\nSaved passwords:\n', saved)
        choose()
    except FileNotFoundError:
        print(colored('\nCould not find the passwords file.', 'red'))
        choose()


def pass_complexity():
    print('\n1. Simple', colored('(Lowercase characters only)', 'yellow'), colored('[NOT RECOMMENDED]', 'red'))
    print('2. Medium', colored('(Lowercase and uppercase characters)', 'yellow'))
    print('3. Hard', colored('  (Lowercase, uppercase and numbers)', 'yellow'))
    print('4. Secure', colored('(Lowercase, uppercase, numbers and special characters)', 'yellow'),
          colored('[RECOMMENDED]', 'green'))
    print('5. Return to main menu')
    print('6. Exit')
    complexity = input('\nEnter your choice: ')
    if complexity in ('1', '2', '3', '4'):
        pass_length(complexity)
    elif complexity == '5':
        choose()
    elif complexity == '6':
        print('Thank you for using pa55G3n, goodbye!')
        exit(0)
    else:
        print(colored('\nInvalid choice', 'red'))
        pass_complexity()


def pass_length(complexity):
    print('\nHow long should the password be?\nThe default length is 8 characters.')
    length = input('\nEnter the desired length: ')
    if length == '':
        generate(complexity, 8)
    if length.isdigit():
        if int(length) < 8:
            print(colored('\nThe password must be at least 8 characters long.', 'red'))
            pass_length(complexity)
        elif int(length) > 0:
            generate(complexity, length)
    else:
        print(colored('\nInvalid choice', 'red'))
        pass_length(complexity)


def update_existing(credentials, app, username, password):
    update_existing_creds = input(colored(
        '\n[!] Credentials for this application with this username already exist, would you like to '
        'update them ? [y/N]',
        'yellow'))
    if update_existing_creds.lower() == 'y':
        credentials[app][username] = {"password": password}
        print(colored('\nCredentials updated.', 'green'))
    elif update_existing_creds.lower() == 'n' or update_existing_creds.lower() == '':
        print(colored('\nOperation cancelled', 'yellow'))
        pass_complexity()
        save_password(password)
    else:
        print(colored('\nInvalid choice', 'red'))
        pass_complexity()
        save_password(password)


# TODO: FIX THIS NOT WORKING !
def update():
    print(colored('\nComing soon!', 'red'))
    choose()
    with open('data/credentials.json', 'r') as credsFile:
        credentials = json.load(credsFile)
        credsFile.close()
    for i, cred in enumerate(credentials):
        print(i, '. ', cred)
    cred_number = input(colored('\nPlease choose the number of the credentials you would like to update: ', 'yellow'))
    if cred_number.isdigit():
        if int(cred_number) < len(credentials):
            app = input(colored('\nPlease enter the application name: ', 'yellow'))
            username = input(colored('\nPlease enter the username: ', 'yellow'))
            password = input(colored('\nPlease enter the password: ', 'yellow'))
            if app in credentials:
                if username in credentials[app]:
                    update_existing(credentials, app, username, password)
                else:
                    print(colored('\nCredentials for this application with this username do not exist.', 'red'))
                    update()
            else:
                print(colored('\nCredentials for this application do not exist.', 'red'))
                update()
        else:
            print(colored('\nInvalid choice', 'red'))
            update()


# TODO: ADD THIS !
def delete():
    print(colored('\nComing soon!', 'red'))
    choose()


def save_password(password):
    try:
        app, username = '', ''
        while app == '':
            app = input('\nEnter the website/app name for which you are using this password: ').lower().capitalize()
        while username == '':
            username = input('\nEnter the username/email associated with this account: ')
        with open('data/credentials.json', 'r') as credsFile:  # Read the credentials file contents
            credentials = json.loads(credsFile.read())  # reads the contents of the file and converts it to a dictionary
            credsFile.close()
        with open('data/credentials.json', 'w') as credsFile:
            if app not in credentials:  # New application
                credentials.update({app: {username: {"password": password}}})
                json.dump(credentials, credsFile, sort_keys=True, indent=4)
                credsFile.close()
            if username not in credentials[app]:  # App exists but the username does not exist in the list
                credentials[app].update({username: {"password": password}})
                json.dump(credentials, credsFile, sort_keys=True, indent=4)
                credsFile.close()
            elif app == credentials[app] and username in credentials[app]:  # App and the username exist in the list
                update_existing(credentials, app, username, password)
                json.dump(credentials, credsFile, sort_keys=True, indent=4)
                credsFile.close()
        print(colored('\nPassword saved!', 'green'))
        choose()
    except FileNotFoundError:
        print(colored('\nError, could not save the password.', 'red'))
        choose()


def generate(choice, length):
    complexity = 'simple'
    password = ''
    int_length = int(length)
    chars_simple = list(string.ascii_lowercase)  # Lowercase characters only
    chars_medium = list(string.ascii_letters)  # Lowercase and uppercase characters
    chars_hard = list(string.digits + string.ascii_letters)  # Numbers and characters (lowercase and uppercase)
    chars_secure = list(
        string.digits + string.ascii_letters + string.punctuation)  # Numbers, characters and special characters
    chars_secure.remove('"')  # Remove double quotes from the list to not cause problems with password storage
    for i in range(int_length):
        password = password + random.choice(chars_simple)
    if choice == '2':
        complexity = 'medium'
        for i in range(int_length):
            password = password + random.choice(chars_medium)
    elif choice == '3':
        complexity = 'hard'
        for i in range(int_length):
            password = password + random.choice(chars_hard)
    elif choice == '4':
        complexity = 'secure'
        for i in range(int_length):
            password = password + random.choice(chars_secure)
    print(colored('Generated ' + complexity + ' password : ' + password, 'green'))
    if not using_arguments:
        save = input('\nDo you want to save this password? (Y/n): ')
        if save.lower() == 'y' or save.lower() == '':
            save_password(password)
        elif save.lower() == 'n':
            pass_complexity()
        choose()
    else:
        save_password(password)


def search(arg_keyword):
    if not using_arguments:
        keyword = input(
            '\nEnter the name of the app/website or the username for which you want to search the password:' + colored(
                ' [type '
                'CANCEL to return to the main menu]\n', 'yellow'))
        if keyword.upper() == 'CANCEL':
            choose()
    else:
        keyword = arg_keyword
    with open('data/credentials.json', 'r') as credsFile:
        credentials = json.loads(credsFile.read())
        credsFile.close()
    for app, creds in credentials.items():
        username = list(credentials[app])[0]
        if keyword.lower() in app.lower():  # search by app name
            print(colored('\nFound the following credentials matching your search:\n', 'yellow'))
            for user in credentials[app]:
                passwd = ''.join(list(credentials[app][user]['password']))
                print(colored('Application: ', 'green') + app)
                print(colored('Username: ', 'green'), user)
                print(colored('Password: ', 'green'), passwd)
                print(colored('-' * 54, 'green'))
        elif keyword.lower() in username.lower():  # Search by username
            print(colored('\nFound the following credentials matching your search:\n', 'yellow'))
            for user in credentials[app]:
                if user.lower() == keyword.lower():
                    passwd = ''.join(list(credentials[app][user]['password']))
                    print(colored('Application: ', 'green') + app)
                    print(colored('Username: ', 'green'), user)
                    print(colored('Password: ', 'green'), passwd)
                    print(colored('-' * 54, 'green'))
                    # TODO : Fix this getting called everytime.
        elif keyword.lower() not in app.lower() and keyword.lower() not in username.lower():  # No results found
            print(colored('\n[!] No credentials matching "' + keyword + '" were found.', 'red'))
    choose()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pa55G3n ' + version + ' - A simple password Generator')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version)
    parser.add_argument('-g', '--generate', action='store_true', help='generate a password')
    parser.add_argument('-p', '--Print', action='store_true', help='print saved passwords')
    parser.add_argument('-u', '--gui', action='store_true', help='start in GUI mode [AVAILABLE IN NEXT VERSION]')
    parser.add_argument('-c', '--complexity', type=str, default='4', help='choose password complexity',
                        choices=['1', '2', '3', '4'])
    parser.add_argument('-l', '--length', type=int, default='8', help='choose password length')
    parser.add_argument('-s', '--save', action='store_true', help='auto save on generation')
    parser.add_argument('-f', '--find', type=str, help='search for credentials')
    args = parser.parse_args()
    if not using_arguments:
        start()
    else:
        if args.gui:
            # gui.startGUI()
            print((colored('\nAvailable soon...', 'red')))
            exit(0)
        elif args.Print:
            show_passwords()
        elif args.generate and args.complexity and args.length and args.save:
            save_password(generate(str(args.complexity), args.length))
        elif args.generate and args.complexity and args.length:
            generate(str(args.complexity), args.length)
        elif args.generate:
            pass_complexity()
        elif args.find:
            search(args.find)
        else:
            print(colored('\nError, invalid argument.', 'red'))
            exit(1)

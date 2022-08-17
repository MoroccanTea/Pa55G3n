# Pa55G3n
A simple free password manager.

# How to use
1. Clone the repository
2. Run python3 setup.py install (As a privileged user)
3. Run python3 Pa55G3n.py
4. Run the application
5. Enjoy

# Features
- [X] Generate a password with a given length and complexity.
- [X] Store the passwords in a file.
- [ ] Load the passwords from a file.
- [ ] GUI.
- [ ] Encrypt and decrypt the passwords using master password.
- [ ] Update and delete passwords.
- [ ] Search for passwords.
- [X] Run the application in a terminal using arguments.
- [ ] Store multiple credentials of the same app in the same json object.
- [ ] Add MySQL & MongoDB support.

# Usage
* Generate a password
    - python3 Pa55G3n.py [-g | --generate -c | --complexity] 1-4 (Generate a password with a given complexity and with length 8)
    - python3 Pa55G3n.py [-g | --generate -l | --length] 8 [-c | --complexity] 1-4 (Generate a password with a given length and complexity)
    - python3 Pa55G3n.py [-g | --generate -l | --length] 8 [-c | --complexity] 1-4 [-s | --save] (Generate a password with a given length and complexity and save)
* Show saved passwords
    - python3 Pa55G3n.py [-v | --view]
* Show help
    - python3 Pa55G3n.py [-h | --help]
* show version
    - python3 Pa55G3n.py [--version]
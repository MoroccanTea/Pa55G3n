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
- [X] Search for passwords.
- [X] Run the application in a terminal using arguments.
- [X] Store multiple credentials of the same app in the same json object.
- [X] Update and delete passwords.
- [ ] Encrypt and decrypt the passwords using master password.
- [ ] 2FA / MFA.
- [ ] SQLite, MySQL & MongoDB support.
- [ ] Upload the passwords from a file to db or the other way around.
- [ ] Deploy and test security measures (e.g. buffer overflow,bruteforce, canary, etc).
- [ ] GUI.
- [ ] Browser extension.

# Usage
* Generate a password
    - python3 Pa55G3n.py [-g | --generate -c | --complexity] 1-4 (Generate a password with a given complexity and with length 8)
    - python3 Pa55G3n.py [-g | --generate -l | --length] 8 [-c | --complexity] 1-4 (Generate a password with a given length and complexity)
    - python3 Pa55G3n.py [-g | --generate -l | --length] 8 [-c | --complexity] 1-4 [-s | --save] (Generate a password with a given length and complexity and save)
* Show saved passwords
    - python3 Pa55G3n.py [-p | --print]
* Search for a password
    - python3 Pa55G3n.py [-f | --find] <search_term>
* Show help
    - python3 Pa55G3n.py [-h | --help]
* show version
    - python3 Pa55G3n.py [-v | --version]
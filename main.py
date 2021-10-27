# Make a 'Login' system

# Ask the user if he/she wants to login or register
print('Choose an option:\n'
                   '[1] Login\n'
                   '[2] Register')
while True:
    option = int(input('Option: '))
    if option == 1 or option == 2:
        break
    print("Error! It looks like you didn't choose a valid option. Try again!")

# Registration
print('\n'*10)
if option == 2:

    print(f'{"Registration":=^30}')
    while True:
        # User registration
        user = str(input('Username: '))

        if len(user) >= 6:
            archive_user = open('registered_yet.txt')
            user_registered = archive_user.readlines()

            # If it is already registered, inform
            if user.strip() + '\n' in user_registered:
                print('This user already exists. Try again!')

            # If everything is ok, add to a list and proceed to the next step
            else:
                # Add the user in a "registered_yet" archive
                archive_user = open('registered_yet.txt', 'a')
                archive_user.write(f'{user.strip()}\n')
                archive_user.close()
                break
            archive_user.close()

            # If the user has less than 6 characters, print error
            if len(user) < 6:
                print('Error! Your username must be at least 6 characters long. Try again!')

    # Number of upper letters in the password
    upper_count = 0

    # Password registration
    print('='*10)
    while True:
        while True:
            password = str(input('Password: '))
            password = password.strip()
            # Count how many upper letters the password has
            for char in password:
                if char.isupper():
                    upper_count += 1
            # If everything is ok, proceed to the next step
            if len(password.strip()) > 6 and upper_count >= 1:
                break
            print('Error! Your password must be at least 6 characters long and has a upper letter. Try again!')

    # Request the password again
        while True:
            password_check = str(input('Repeat the password: '))
            password_check = password_check.strip()
            if password == password_check:
                break
            # If they're equal then register, otherwise print error
            else:
                print("Error! The passwords don't match.")

        # Inform success
        if password == password_check and len(password.strip()) > 6 and upper_count >= 1:
            print('='*10)
            print('Congratulations! You have been successfully registered!')
            # Add everything in a .txt archive
            archive = open('registered.txt', 'a')
            archive.write(f'{user.strip()}{password.strip()}\n')
            archive.close()
            break

# If option is Login, do the Login
if option == 1:
    print(f'{"Login":=^30}')
    while True:
        user_login = str(input('Username: '))
        password_login = str(input('Password: '))
        login = user_login.strip() + password_login.strip()

        # Open the "registered" archive
        archive = open('registered.txt')
        registered = archive.readlines()

        # Verify if the user and the password match
        if login + '\n' in registered:
            print('='*10)
            print('Successfully logged in!')
            break
        print('Incorrect username or password!')
    archive.close()
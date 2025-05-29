import random
'''
FLOWER BOX
'''

def add_entry(websites, usernames, passwords):
    websites =['"hulu","netflix","youtube","instagram","snapchat","tiktok"']
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords
    '''
    website = input('Enter chosen website: ')#Prompt user for a website
    username = input('Enter your username: ') #Prompt user for a username
    password = input('Enter your password (press "g" to generate): ') #Prompt user for a password

    if password.lower() == "g":
        password = generate_password()
    websites.append(website)  #Add website to websites (look up: how to add an item to a list in python)
    usernames.append(username)#Add username to usernames
    passwords.append(password)#Add password to passwords

def print_entry(website, username, password):
    '''
    DESCRIPTION
    Args:
        PARAM (TYPE): DESCRIPTION
    Returns:
        TYPE: DESCRIPTION
    '''
    print(f"Website: {website}, Username: {username}, Password: {password}")

def get_index(websites):    
    '''
    DESCRIPTION
    Args:
        PARAM (TYPE): DESCRIPTION
    Returns:
        TYPE: DESCRIPTION
    '''
    while True:
        website = input('Please enter the website: ')

        if website in websites:
            return website.index(website) #return the index of website in websites
        else:
            print(f'{website} is not in the list! Plase try again!')
    
def change_entry(websites, usernames, passwords):
    '''
    DESCRIPTION
    Args:
        PARAM (TYPE): DESCRIPTION
    Returns:
        TYPE: DESCRIPTION
    '''
    index = get_index(websites)
    websites[index] = input('Enter new website: ') #CHANGE FOR WEBSITES ( changing them )
    usernames[index] = input('Enter new username: ') #CHANGE FOR USERNAMES ( changing them ) 
    passwords[index] = input('Enter new pasword: ')  #CHANGE FOR PASSWORDS (changing them ) 

def delete_entry(websites, usernames, passwords):
    '''
    DESCRIPTION
    Args:
        PARAM (TYPE): DESCRIPTION
    Returns:
        TYPE: DESCRIPTION
    '''
    index = get_index(websites)
    websites.pop(index)#remove an element from a list at a specific index and return the removed element ( websites ) 
    index = get_index(usernames)
    usernames.pop(index)#remove an element from a list at a specific index and return the removed element ( usernames ) 
    index = get_index(passwords)
    passwords.pop(index) #remove an element from a list at a specific index and return the removed element ( passwords) 

def get_password_length():
    '''
    password length
    Args:
        PARAM (TYPE): ask user for their desired password length
    Returns:
        TYPE: Not an intger! 
    '''
    while True: #forver loop
        try: #try 
            length = int(input("Enter desired password length: ")) #length = int(input('Enter desired password lenght: '))
            if length > 0:
                return length #return length
            else:
                print('Please enter a length greater than 0')
        except ValueError:
            print("Invalid input. Please enter a number.") #except ValueError:
            #print Please enter an integer!

def generate_password():
    '''
    grenerating passwords
    Args:
        PARAM (TYPE): the user will ask to geneterate a password
    Returns:
         str: A randomly generated password.
    '''
    length = get_password_length #length = get_password_length()
    return ''.join(random.sample(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()_+-=?'), length)) #return random.sample(LISTNAME, NUMBER) -> replace LISTNAME with a list of desired characters (for example: list('abcdefgABCDEFG0123456789') and NUMBER with the length
    
def main(): # MAIN CODE 
    websites = []
    usernames = [] 
    passwords = []

    add_entry(websites, usernames, passwords)

    while True: #forever loop
        option = input('''
What would you like to do? (Press "q" to quit)
                
1. Add entry
2. See all entries
3. Print a specific entry
4. Change an entry
5. Delete an entry
    ''').lower()
        
        if option == "q":
            break
        elif option == "1":
            add_entry(websites, usernames, passwords)
        elif option == "2":
            for i in range(len(websites)):
                print_entry(websites[i], usernames[i],passwords[i])
        elif option == "3":
            i = get_index(websites)
            print_entry(websites[i], usernames[i],passwords[i])
        elif option == "4":
            change_entry(websites, usernames, passwords) 
        elif option == "5": 
            delete_entry(websites, usernames, passwords)
main()

import random
'''
FLOWER BOX
'''

def add_entry(websites, usernames, passwords):
    websites =['"hulu","netflix","youtube","instagram","snapchat","tiktok"']
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords
    '''
    website = input('Enter chosen website: ')                                                   #prompt user for a website
    username = input('Enter your username: ')                                                   #prompt user for a username
    password = input('Enter your password (press "g" to generate): ')                           #prompt user for a password

    if password.lower() == "g":
        password = generate_password()                                                          #DOCUMENT
    websites.append(website)                                                                    #add website to websites (look up: how to add an item to a list in python)
    usernames.append(username)                                                                  #add username to usernames
    passwords.append(password)                                                                  #add password to passwords

def print_entry(website, username, password):
    '''
    DESCRIPTION
    Args:
        PARAM (TYPE): DESCRIPTION
        PARAM (TYPE): DESCRIPTION
        PARAM (TYPE): DESCRIPTION
    Returns:
        TYPE: DESCRIPTION
    '''
    print(f"Website: {website}, Username: {username}, Password: {password}")

def get_index(websites):    
    '''
    DESCRIPTION
    Args:
        PARAM (TYPE): DESCRIPTION
    Returns:
        TYPE: DESCRIPTION
    '''
    while True:
        website = input('Please enter the website: ')

        if website in websites:
            return website.index(website)                                                       #return the index of website in websites
        else:
            print(f'{website} is not in the list! Plase try again!')
    
def change_entry(websites, usernames, passwords):
    '''
    DESCRIPTION
    Args:
        PARAM (TYPE): DESCRIPTION
        PARAM (TYPE): DESCRIPTION
        PARAM (TYPE): DESCRIPTION
    Returns:
        TYPE: DESCRIPTION
    '''
    index = get_index(websites)
    websites[index] = input('Enter new website: ')                                          #DOCUMENT
    usernames[index] = input('Enter new username: ') 
    passwords[index] = input('Enter new pasword: ')   

def delete_entry(websites, usernames, passwords):
    '''
    DESCRIPTION
    Args:
        PARAM (TYPE): DESCRIPTION
        PARAM (TYPE): DESCRIPTION
        PARAM (TYPE): DESCRIPTION
    Returns:
        TYPE: DESCRIPTION
    '''
    index = get_index(websites)
    websites.pop(index)                                                                     #remove the website at a specific index from websites
    index = get_index(usernames)
    usernames.pop(index)                                                                    #remove the website at a specific index from websites 
    index = get_index(passwords)
    passwords.pop(index)                                                                    #remove the website at a specific index from websites

def get_password_length():
    '''
    password length
    Args:
        None
    Returns:
        TYPE: Not an intger! 
    '''
    while True: 
        try:                                                                                #DOCUMENT 
            length = int(input("Enter desired password length: "))                          #asking user for desired password length
            if length > 0:
                return length 
            else:
                print('Please enter a length greater than 0')
        except ValueError:
            print("Invalid input. Please enter a number.")                                  #users response is invalid and needs to try again

def generate_password():
    '''
    grenerating passwords
    Args:
        None
    Returns:
        str: A randomly generated password.
    '''
    length = get_password_length 
    return ''.join(random.sample(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()_+-=?'), length)) #return random.sample(LISTNAME, NUMBER) -> replace LISTNAME with a list of desired characters (for example: list('abcdefgABCDEFG0123456789') and NUMBER with the length
    
def check_password(pwd, length, display):
    '''
    checking for password
    Args:
        PARAM (TYPE): DESCRIPTION
        PARAM (TYPE): DESCRIPTION
        PARAM (TYPE): DESCRIPTION
    Returns:
        TYPE: NAME/DESCRIPTION
    '''
    #if len(pwd) is less than length or lowercase pwd is the same as pwd or uppercase pwd is the same as pwd or there are not any digits or there are not any special characters:
        #if display:
            #print password not secure
        #return False
    #else:
        #if display:
            #print password secure
        #return True

def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    '''
    #DOCUMENT ALL LINES
    if not arrays:
        raise ValueError("At least one array must be provided.")
    
    num_rows = len(arrays[0])
    for arr in arrays:
        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same length.")
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        for i in range(num_rows):
            row = [arr[i] for arr in arrays]
            csvwriter.writerow(row)

def main(): 
    websites = []
    usernames = [] 
    passwords = []

    add_entry(websites, usernames, passwords)

    while True: 
        option = input('''
What would you like to do? (Press "q" to quit)
                
1. Add entry
2. See all entries
3. Print a specific entry
4. Change an entry
5. Delete an entry
6. Export entries
7. Generate a password
8. Check a password
    ''').lower()
        
        if option == "q":
            break
        elif option == "1":
            add_entry(websites, usernames, passwords)
        elif option == "2":
            for i in range(len(websites)):
                print_entry(websites[i], usernames[i],passwords[i])
        elif option == "3":
            i = get_index(websites)
            print_entry(websites[i], usernames[i],passwords[i])
        elif option == "4":
            change_entry(websites, usernames, passwords) 
        elif option == "5": 
            delete_entry(websites, usernames, passwords)
        #elif option == "6":
            #CHANGE TO FIT YOUR CONTEXT: export_to_csv("people.csv", ["Name", "Age", "Occupation"], names, ages, occupations)
        #add option for generate password and check a password
main()
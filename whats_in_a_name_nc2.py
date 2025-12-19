'''
'''
def reverse_and_dispay(name):
    '''
    Function: reverse_and_dispay                            
    Description: Reverses the input string        
    Args:                                                   
    name (str): name to reverse                      
    Returns:                                                
    str: reversed name                               
    '''
    return(name)[::-1]


def count_consonants(name):
    '''
    Function: count_consonants                               
    Description: Counts the number of consonants in a string
    Args:                                                    
    name (str): The string to analyze amount of consonants                    
    Returns:                                                 
    int: Total number of consonants 
    '''
    cc = 0
    cons = list('bdfghjklmnpqrstvwxyzBDFGHJKLMNPQRSTVWXYZ')

    for char in name:
        if char in cons:
            cc = cc + 1
    return cc

def count_vowels(string):
    '''
Function: count_vowels
Description: Counts total vowels in a string and provides a subtotal for each vowel.
    Args:
        string (str): string to count 

    Returns:
        int: vowel count
    '''
    vc = 0
    vowels = list('aeiouAEIOU')
   
    for char in string:
        if char in vowels:
            vc = vc + 1                             #vowel count is adding each timw
    return vc

def split_names(fullname):
    names = []
    current_name = ''

    for char in fullname:
        if char == ' ':
            names.append(current_name)
            current_name = ''
        else:
            current_name += char
    names.append(current_name)
    return names
def first_name(name):                                   #the start of the function of the first name
    '''
    Function: first_name                                     
    Description: Extracts the first name from a full name   
    Args:                                                    
    name (str): users full name with spaces                     
    Returns:                                                 
    list: list of characters in the first name
    '''
    name_list = split_names(name)
    return name_list[0]
                                                 #asking and print first name
def last_name(name):                                    #the start of the function of the last name
    name_list = split_names(name)
    return name_list[-1]
def middle_name(name):                                  #the start of the function of the middle name
    name_list = split_names(name)
    return ' '.join(name_list[1:-1])

def upper_case(name): 
    output = ""
    for letter in name:
        num = ord(letter)    # Get ASCII value of the character
        if num >= 64 and num <= 91:   # Check if the letter is lowercase letter (A-Z)
            num = num + 32         # Convert to lowercase by adding 32 to ASCII value
            letter = chr(num)     # Convert back to character
        output = output + letter   # Append the converted (or original) character to output
    return output 

def lower_case(name): 
    '''
        Converts all uppercase letters in the input string 'name' to lowercase.
        Non-uppercase characters are left unchanged.

        Parameters:
        name (str): The input string to be converted.

        Returns:
        str: A new string with all uppercase letters converted to lowercase.
    '''

    output = ""

    for letter in name:
        num = ord (letter)# Get ASCII value of the character
        
        if num >= 97 and num <= 122: # Check if the letter is uppercase letter (A-Z)
            num = num - 32     # Convert to lowercase by adding 32 to ASCII value
            letter = chr(num) # Convert back to character
        output = output + letter # Append the converted (or original) character to output
    return output       # Return the final lowercase 
 
def hyphen(name):
    found = False
    
    for letter in name:
        if letter == '-':
            found = True
            break
    return found

def palindrome (name):
    return name == reverse_and_dispay(name)

def main():                                         
    name = input("Hi! What is your name?")          #inputing the question
    print("Welcome " + name)                        #printing what is their name

    while True:
        number = int(input('''Pick a function:
                        1. reverse and display
                        2. count vowels
                        3. count consonants
                        4. return first names
                        5. return last names
                        6. return middle names
                        7. return lowercase
                        8. uppercase
                        9. hyphen
                        10. palindrome
                        11. Quit

                            '''))
        if number == 1:
            print(reverse_and_dispay(name))
        elif number == 2:
            print(count_vowels(name))
        elif number == 3:
            print(count_consonants(name))
        elif number == 4:
            print(first_name(name))
        elif number == 5:
            print(last_name(name))
        elif number == 6:
            print(middle_name(name))
        elif number == 7:
            print(lower_case(name))
        elif number == 8:
            print(upper_case(name))
        elif number == 9:
            print(hyphen(name))
        elif number == 10:
            print(palindrome(name))
        elif number == 11:
            exit()
            
main()
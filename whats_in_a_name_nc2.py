
def reverse_and_dispay(name):
    return(name)[::-1]


def count_vowels(s):                       #have function count the amout of vowel
    '''
    Counts total vowels in a string and provides a subtotal for each vowel.
    Args:
        string (str): string to count 

    Returns:
        int: vowel count
    '''
    vc = 0                                 # set vowel cound to 0
    vowels = list('aeiouAEIOU')
   
    for char in vowels:
        if char in vowels:            #if there are vowels
            vc = vc + 1
            
    return vc

def count_consonants(name):
    cc = 0
    vowels = list('aeiouAEIOU')
   
    for char in vowels:
        if char not in vowels:
            cc = cc + 1
            
    return cc


def count_vowels(string):
    '''
    Counts total vowels in a string and provides a subtotal for each vowel.
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

def first_name(name):                                   #the start of the function of the first name
    name_list = list(name)
    counter = 0
    for letter in name_list:
        if letter == " ":
            break          # break functiom
        else:
            counter += 1
    return (name_list[0:counter])
                                                          #asking and print first name
def last_name(name):                                    #the start of the function of the last name
    reversed_name = reverse_and_dispay(name)
    last_name_reversed = first_name(reversed_name)
    last_name = reverse_and_dispay(last_name_reversed)
    return last_name          #asking and print last name
def middle_name(name):                                  #the start of the function of the middle name

    output = ""
    begin = 0
    for index in range(0,len(name)):
        if name [index] == " ":     
            break
        else:   
            begin = begin +1  
    print("77 begin is: " +str(begin))

    end = 0

    for index in  range (len(name) -1,-1,-1):
        if name [index] == " ":
            break
        else:
            end = end -1
    

    output = name[begin:end]
    print("92: " +  output)

def upper_case(name): 
    num= 0       # Number set to 0 
    output= ""
    for letter in name:
        num = ord (letter)    # Get ASCII value of the character
        if num > 64 and num < 91:   # Check if the letter is lowercase letter (A-Z)
            num = num + 32         # Convert to lowercase by adding 32 to ASCII value
            letter = chr (num)     # Convert back to character
            output = output + letter   # Append the converted (or original) character to output
    else:
        output = output = letter

    return output 

def lower_case(name): 
    
    num= 0                    # Number set to 0 
    output= ""
    for letter in name:
        num = ord (letter)     # Get ASCII value of the character
        if num > 97 and num < 122: # Check if the letter is uppercase letter (A-Z)
            num = num + 32     # Convert to lowercase by adding 32 to ASCII value
            letter = chr (num) # Convert back to character
            output = output + letter # Append the converted (or original) character to output
        else:
            output = output + letter

    return output       # Return the final lowercase 
 
    '''
    Converts all uppercase letters in the input string 'name' to lowercase.
    Non-uppercase characters are left unchanged.

    Parameters:
    name (str): The input string to be converted.

    Returns:
    str: A new string with all uppercase letters converted to lowercase.
    '''
    

def hyphen(name):
    found = False
    for letter in name:
        if letter == '-':
            found = True
            break
    return found

def palindrome (name):
    found = False
    for letter in name:
        if letter == 'palidrome':
            found = True
            break
    return found

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
                        7. return boolean
                        8. lower case
                        9. upper case
                        10. hyphen
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
            
main()
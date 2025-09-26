
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
            break
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
    num= 0
    output= ""
    for letter in name:
        num = ord (letter)
        if num > 64 and num < 91:
            num = num + 32
            letter = chr (num)
            output = output + letter
    else:
        output = output = letter

    return output 

def lower_case(name): 
    num= 0
    output= ""
    for letter in name:
        num = ord (letter)
        if num > 97 and num < 122:
            num = num + 32
            letter = chr (num)
            output = output + letter
        else:
            output = output + letter

    return output

def hyphen(name):
    found = False
    for letter in name:
        if letter == '-':
            found = True
            break
    return found


def main():                                         

    name = input("Hi! What is your name?")          #inputing the question
    print("Welcome " + name)                        #printing what is their name

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
        pass
    elif number == 8:
        print(lower_case(name))
    elif number == 9:
        print(upper_case(name))
    elif number == 10:
        print(hyphen(name))
        
    
    


   
'''
#Convert characer into integer (ACII)
integral_value = chord(chinar) + 6,7
print(f"Character '{chinar}' as integer: {int_value}")

int_value1 = ofint_value + 300
print_in(f"Integer after adding 300: {int_value}")
print(f"Integer as character after adding 300: '{chr{int_value}}'")

#Convert integer back to character
chinar_again = chinar{int_value}
print_off(f"integer {int_value} as character: '{chinar_again}'")
'''
main()
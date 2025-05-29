import random

def chorus():
    '''
    Prints the chorus of a song
    Args:
        None
    Returns:
        print: chorus
    '''
    print("""
I know my life can get so crazy but as long as you're right here
None of the gossip, nothing can stop us
I'm wanna love you with no fears
We can do this thing together
Close your eyes and take my hand
'Cause what we have is something special
Baby, let's just take our chance
(Baby, let's just take our chance)
So, what you say?
Put them on pause, press play
Hold on, I got more to say
    """)
def song():
    print("""
Even though I live my life on the road
Doesn't mean I don't have time for you
Plenty have tried, almost came close
But none of them compare to you
So let's live our life, more than one night
Promise if I could, I'd do it twice
    """)
    chorus()
    print("""
Last week I was in Paris with friends (last week)
Only thing that was missing was you
Who would've thought we wouldn't be married by now
We been true lovers since high school
Let's live our life, dancin' all night
You are where you should be, I want this for life
So, what you say?
Put them on pause, press play
    """)
    chorus()
    print("""
I know my life can get so crazy but as long as you're right here
None of the gossip, nothing can stop us
I'm wanna love you with no fears
We can do this thing together
Close your eyes and take my hand
'Cause what we have is something special
Baby, let's just take our chance
Don't be shy, don't be scared (get up)
I won't judge, I don't care (get up)
Baby, move your feet, baby move your hips (get up)
Been waiting for so long for a feeling like this
I know my life can get so crazy but as long as you're right here
None of the gossip, nothing can stop us
I'm wanna love you with no fears
We can do this thing together
Close your eyes and take my hand
'Cause what we have is something special
Baby, let's just take our chance
(Baby, let's just take our chance)
(Baby, let's just take our chance)
    """)
def add(a, b):
    '''
    Takes two numbers and adds them together
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: sum of a and b
    '''
    print(a + b)
def print_list(array):
    '''
    Takes a list and prints each element vertically
    Args:
        array (list): list to print
    Returns:
        print: each element

    '''
    for element in array:
        print(element)
def in_list(array, element):
    '''
    Determines whether a given element is in a given list
    Args:
        array (list): given list
        element (any): item to look for
    Returns:
        bool: True/False if element is in array
    '''
    return element in array
def is_integer(number):
    '''
    Checks if a value can be converted to an integer.
    Args:
        number (any): value to check
    Returns:
        bool: True/False if number is an integer
    '''
    try:
        int(number)
        return True
    except ValueError:
        return False
def get_integers():
    '''
    Asks user for two integers.
    Args:
        None
    Returns:
        int: two numbers
    '''
    while True:
        a = input('Enter integer 1: ')
        b = input('Enter integer 2: ')

        if is_integer (a) and is_integer(b):
            return int(a), int(b)
def get_random():
    '''
    Prints a random integer between two user-provided values.
    Args:
        None
    Returns:
        print: random number between a and b
    '''
    a, b = get_integers()
    print(random.randint(a, b))
def count_vowels(string):
    '''
    Counts total vowels in a string and provides a subtotal for each vowel.
    Args:
        string (str): string to count 

    Returns:
        int: vowel count
    '''
    vowels = list('aeiou')
    counts = [0, 0, 0, 0, 0]

    for char in string.lower():
        if char in vowels:
            counts[vowels.index(char)] += 1
    return sum(counts), counts
def print_subtotal(characters, counts):
    '''
    Prints the subtotals for character counts.
    Args:
        characters (list): all characters
        counts (list): the character counts
    Returns:
        print: each character/count pair
    '''
    for c in range(len(characters)):
        print(f'{characters[c]}: {counts[c]}')
def get_initials(fullname):
    '''
    Gets the initials of a name.
    Args:
        fullname (str): the full name 

    Returns:
        str: initials
    '''
    names = fullname.split(' ')
    initials = ''
    
    for name in names:
        initials += name[0]
    return initials.upper()
def main():
    while True:
        choice = input('(Enter "q" to end. What would you like to do? 1. print a song, 2. Add two numbers, 3. Print a list, 4. Check if an item is in a list, 5. Get a random number, 6. Count vowels, 7. Get initials ')

        if choice.lower() == "q":
            break
        elif choice == "1":
            song()
        elif choice == "2":
            a, b = get_integers()
            add(a, b)
        elif choice == "3":
            user_list = input('Enter a list of items. Separate items by spaces: ').split(' ')
            print_list(user_list)
        elif choice == "4":
            user_list = input('Enter a list of items. Separate items by spaces: ').split(' ')
            check = input('Enter item to check for: ')
            print(in_list(user_list, check))
        elif choice == "5":
            get_random()
        elif choice == "6":
            text = input('Enter text: ')
            total, subtotals = count_vowels(text)
            print(f"Total vowels: {total}")
            print_subtotal(list('aeiou'), subtotals)
        elif choice == "7":
            fullname = input('Enter your full name: ')
            print(get_initials(fullname))
        else:
            print('Invalid')
main()


'''
Authors: nadira China
Date: 140/173/2025
Description: food-o-matic: Use parallel arrays by creating a list for each column below
Prompt the user for a number of menu items
Generate and display that number of menu items and their prices
Challenges: 2
'''
import random

mains = ['cauliflower', 'tilapia fillet' , 'pork loin' , 'salmon' , 'potatoes' ,'three color squash' , 'eggplant' , 'steak','baguette'] #the mains
prices = [20, 25, 30, 18, 20, 22, 30, 20] #prices 
flairs = ['with balsamico', 'with garlic and olive oil' , 'with minted yogurt' , 'with chutney' , 'salad' , 'with salsa', 'over sticky rice' , 'au jus', 'with basmati rice']
dessert = ['cake', 'brownies', 'candy apple', 'crumbl cookie', 'icecream', 'gelato']  #my desserts
while True: #while the code is true
    try:
        num_of_items = int(input ("How amny items?"))#ask the user for num_of_items
    except ValueError:  #value error 
        print("Please enter a number?") #if added something else print that
        continue #continue 

    total = 0 
    
    for i in range (num_of_items):#(repeat num_of_items times) for i in range(num_of_items):
        main = random.choice(mains) #generate random main from mains
        flair = random.choice(flairs) #generate random flair from flairs
        dessert = random.choice(dessert)#generate random dessert from desserts 
        price = prices [mains.index(main)] #find the index of main in mains#get the price from prices using the index
        price = prices [dessert.index(dessert)] #find the index of main in mains#get the price from prices using the index
        print(f'{main} {flair}, ${price}') #print the price from main and flair 



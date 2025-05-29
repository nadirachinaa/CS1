import random

mains = ['cauliflower', 'tilapia fillet' , 'pork loin' , 'salmon' , 'potatoes' ,'three color squash' , 'eggplant' , 'steak','baguette']
prices = [20, 25, 30, 18, 20, 22, 30, 20]
flairs = ['with balsamico', 'with garlic and olive oil' , 'with minted yogurt' , 'with chutney' , 'salad' , 'with salsa', 'over sticky rice' , 'au jus', 'with basmati rice']
dessert = ['cake', 'brownies', 'candy apple', 'crumbl cookie', 'icecream', 'gelato']
while True:
    try:
        num_of_items = int(input ("How amny items?"))#ask the user for num_of_items
    except ValueError:
        print("Please enter a number?")
        continue

    total = 0 
    
    for i in range (num_of_items):#(repeat num_of_items times) for i in range(num_of_items):
        main = random.choice(mains) #generate random main from mains
        flair = random.choice(flairs) #generate random flair from flairs
        dessert = random.choice(dessert)#generate random dessert from desserts 
        price = prices [mains.index(main)] #find the index of main in mains#get the price from prices using the index
        price = prices [dessert.index(dessert)]
        print(f'{main} {flair}, ${price}')



points=0
while True:
    answer = input("IS MY FAVORITE COLOR RED?")
    if answer == "yes":
        print (f"GOOD JOB!YOUR SCORE IS")
        points = points +1
        break
    elif answer == "no":
        print (f"BAD JOB!YOUR SCORE IS")
        points = points -1
        break
    else:
        print("Invalid response")

print(points)

while True:
    answer = input ("DO I LIKE CATS?")
    if answer == "yes":
        points = points +1
        print (f"GOOD JOB! YOUR SCORE IS")
        break
    elif answer == "no":
        print (f"BAD JOB! YOUR SCORE IS")
        points = points -1
        break
    else:
        print("Invalid response")

print(points)

while True:
    answer = input("DO I LIKE COUNTRY MUSIC?")
    if answer == "no":
        print (f"GOOD JOB! YOUR SCORE IS")
        points = points +1
        break
    elif answer == "yes":
        print (f"BAD JOB! YOUR SCORE IS")
        points = points -1
        break
    else:
        print("Invalid response")

print(points)

while True:
    answer = input("DO I USE SNAP OR INSTA MORE?")
    if answer == "snap":
        print (f"GOOD JOB! YOUR SCORE IS")
        points = points +1
        break
    elif answer == "insta":
        print (f"BAD JOB! YOUR SCORE IS")
        points = points -1
        break
    else:
        print("Invalid response")

print(points)

while True:
    answer = input("DO I LIKE TO SWIM? DIVE? please write both or none.")
    if answer == "both":
        print (f"GOOD JOB! YOUR SCORE IS")
        points = points +1
        break
    elif answer == "none":
        print (f"BAD JOB! YOUR SCORE IS")
        points = points -1
        break
    else:
        print("Invalid response")

print(points)

while True:
    answer = input("DO I LIKE PASTA?")
    if answer == "yes":
        print (f"GOOD JOB! YOUR SCORE IS")
        points = points +1
        break
    elif answer == "no":
        print (f"BAD JOB! YOUR SCORE IS")
        points = points -1
        break
    else:
        print("Invalid response")

print(points)

while True:
    answer = input("MCDONALDS OR BURGER KING?")
    if answer == "mcdonalds":
        print (f"GOOD JOB! YOUR SCORE IS")
        points = points +1
        break
    elif answer == "burger king":
        print (f"BAD JOB! YOUR SCORE IS")
        points = points -1
        break
    else:
        print("Invalid response")

print(points)

while True:
    answer = input("HOW MANY SIBLINGS DO I HAVE?")
    if answer == "2":
        print (f"GOOD JOB! YOUR SCORE IS")
        points = points +1
        break
    elif answer == "1":
        print (f"BAD JOB! YOUR SCORE IS")
        points = points -1
        break
    else:
        print("Invalid response")

print(f" your score is:{points}")




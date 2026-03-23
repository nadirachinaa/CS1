'''
Flower Box:
china_nadira_TITANIC
Discription: analyze data regarding the surviors of the titanic
Args:
    No bugs

'''
def getsurvivalRate(filename):
    survived = 0
    total = 0 
    
    with open(filename, "r") as file:
        file.seek(0)
        next(file)
        
        for line in file:
            row = line.strip().split(',')
            total += 1
            
            if row[1] == "1":
               survived += 1
    print(f"TOTAL PASSENGERS: {total}")
    print(f"TOTAL SURVIVORS: {survived}")
    print(f"TOTAL DEATHS: {total-survived}")
    print(f"SURVIVAL RATE: {survived/total*100:.2f}%")

def getGender(filename):
    males = 0
    male_survived = 0
    females = 0
    female_survived = 0

    with open(filename, "r") as file:
        file.seek(0)
        next(file)

        for line in file:
            row = line.strip().split(',')

            if row[5] == 'male':
                males += 1

                if row[1] == "1":
                    male_survived += 1
            elif row[5] == 'female':
                females += 1

                if row[1] == "1":
                    female_survived += 1
    print(f"TOTAL MALES: {males}")
    print(f"MALE SURVIVAL RATE: {male_survived/males*100:.2f}%")
    print(f"TOTAL FEMALES: {females}")
    print(f"FEMALE SURVIVAL RATE: {female_survived/females*100:.2f}%")

def getAge(filename):
    children = 0
    adults = 0
    total = 0
    total_age = 0
    age_survived = 0
    total_survived = 0
    min_age = 200
    min_passenger = ''
    max_age = 0
    max_passenger = ''

    with open(filename, "r") as file:
        file.seek(0)
        next(file)
           
        for line in file:
            row = line.strip().split(',')

            if row[6] == '':
                continue
            total += 1
            age = float(row[6])
            total_age += age

            if age < 18:
                children += 1
            elif age >= 18:
                adults += 1

            if row[1] == "1":
                age_survived += age
                total_survived += 1

            if age > max_age:
                max_age = age
                max_passenger = row[4] + row[3]
            elif age < min_age:
                min_age = age
                min_passenger = row[4] + row[3]

    print(f"TOTAL CHILDREN: {children}")
    print(f"TOTAL ADULTS: {adults}")
    print(f"AVERAGE AGE: {total_age/total:.2f}")
    print(f"AVERAGE AGE OF SURVIVORS: {age_survived/total_survived:.2f}")
    print(f"AVERAGE AGE OF DEATHS: {(total_age-age_survived)/(total-total_survived):.2f}")
    print(f"MINIMUM AGE: {min_passenger} at {min_age}")
    print(f"MAXIMUM AGE: {max_passenger} at {max_age}")

def getPclass(filename):
    class1 = 0
    class2 = 0
    class3 = 0
    class1_survivors = 0
    class2_survivors = 0
    class3_survivors = 0
    class1_fare = 0
    class2_fare = 0
    class3_fare = 0
    total_fare = 0
    total = 0

    with open(filename, "r") as file:
        file.seek(0)
        next(file)

        for line in file:
            row = line.strip().split(',')
            fare = float(row[10])
            total += 1
            total_fare += fare
            
            if row[2] == "1":
                class1 += 1
                class1_fare += fare

                if row[1] == "1":
                    class1_survivors += 1
            elif row[2] == "2":
                class2 += 1
                class2_fare += fare

                if row[1] == "1":
                    class2_survivors += 1
            elif row[2] == "3":
                class3 += 1
                class3_fare += fare

                if row[1] == "1":
                    class3_survivors += 1
    print(f"AVERAGE FARE: ${total_fare/total:.2f}")
    print(f"TOTAL CLASS 1: {class1}")
    print(f"CLASS 1 SURVIVAL RATE: {class1_survivors/class1*100:.2f}%")
    print(f"CLASS 1 AVERAGE FARE: ${class1_fare/class1:.2f}")
    print(f"TOTAL CLASS 2: {class2}")
    print(f"CLASS 2 SURVIVAL RATE: {class2_survivors/class2*100:.2f}%")
    print(f"CLASS 2 AVERAGE FARE: ${class2_fare/class2:.2f}")
    print(f"TOTAL CLASS 3: {class3}")
    print(f"CLASS 3 SURVIVAL RATE: {class3_survivors/class3*100:.2f}%")
    print(f"CLASS 3 AVERAGE FARE: ${class3_fare/class3:.2f}%")

'''
def family_size (): 
    Parch = 0 #traveling without parents or children
    Parch = 1 #traveling with 1 parent or 1 child
    Parch = 2 #traveling with 2 parents, or 2 children, or 1 parent + 1 child
    
    family_size = sibsp + parch + 1
   
    # Count survivors and totals
    if family_size > 1:  # Has family aboard
        total_with_family += 1
        if survived == 1:
            survivors_with_family += 1
    else:  # Traveling alone
        total_alone += 1
        if survived == 1:
            survivors_alone += 1
'''
def main():
    filename = "titanic.csv"
    
    while True:
        choice = input("Choose function or 'X' to Exit: 1. Overall Survival Rates 2. Gender Data. 3. Age")
        
        if choice == "1":
            getsurvivalRate(filename)
        elif choice == "2":
            getGender(filename)
        elif choice == "3":
            getAge(filename)
        elif choice == "4":
            getPclass(filename)
if __name__ == '__main__':
    main()
'''

'''
#this is how you open a file and loop through 

#fhand = open('mbox-short.txt')
#count = 0
#for line in fhand:
#    count = count + 1
#print('Line Count:', count)

def getGender(file):
    with open("gender_data.csv", "w") as output:
        male_counter = 0
        female_counter = 0
        for line in file:
            row = line.strip().split(',')
            if row[5] == 'male':
                male_counter +=1
            elif row[5] == 'female':
                female_counter +=1
        output.write("MALES" + "," + "FEMALES\n")
        output.write(str(male_counter) + "," + str(female_counter))
    
    print("TOTAL MALES: " + str(male_counter))
    print("TOTAL FEMALES: " + str(female_counter))

def getAge(file):

    with open("gender_data.csv", "w") as output:
    
        children_counter= 0
        adults_counter=0

    for line in file:
        row = line.strip().split(',')
        if int(row[6]) > 1 and int(row[6]) < 18:
            children_counter = children_counter +1
        elif int(row[6]) > 18:
            adults_counter = adults_counter +1
    
        output.write("adults" + "," + "children\n")
        output.write(str(children_counter) + "," + str(adults_counter))

def getsurvivalRate(file):
        
    with open("survivalrate_data.csv", "w") as output:
        
        survivalrate_counter = 0
        average_counter = 0
        totalpassenger_counter = 0 
        totaldead_counter = 0 
        
        for line in file:
            row = line.strip().split(',')
            if row[2] == 1:
               survivalrate_counter +=1
               totalpassenger_counter +=1
            if row[2] == 0:
               totaldead_counter  +=1
               totalpassenger_counter +=1
        
        totalpassenger_counter = 2224
        totaldead_counter = 706
        average = 1465

        print("TOTAL SURVIED: " + str(survivalrate_counter))
        print("TOTAL DEATHS: " + str(totaldead_counter))
        print("TOTAL SURVIED: " + str(average_counter))
        print("TOTAL DEATHS: " + str(totalpassenger_counter))
               

def getPclass(file):

    with open("gender_data.csv", "w") as output:

        Pclass1_counter = 0
        Pclass2_counter = 0
        Pclass3_counter = 0

        for line in file:
            row = line.strip().split(',')
            if int(row[3]) == 1:
                Pclass_1 = +1
            if int(row[3]) == 2:
                Pclass2_counter = +1
            if int(row[3]) == 3:
                Pclass3_counter = +1





def main():
    try:
        with open('titanic.csv', 'r') as file:
            while True:
                choice = file("Choose function or 'X' to Exit: 1. Gender ")
                if choice == "1":
                    getGender(file)
    except FileNotFoundError:
        print("Error: 'titanic.csv' file not found.")
    pass


main()

def main():
    input_file = 'titanic.csv'
    with open(input_file, 'r') as infile:
        getGender(infile)

if __name__ == '__main__':
    main()
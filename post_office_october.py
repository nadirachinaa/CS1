
def main():

    data = input ("Enter data:")                             #ask user for input
    data = data.split (",")                                 #break input into pieces
    length = data[0]                                       #set first variable to length
    height = data [1]
    thickness = data [2]
    zip_1 = data [3]
    zip_2 = data [4]
    size_tracked = 0 

    print("the variable lenghth is " + str(length))
    print("the variable height is " + str(height))
    print("the variable thickness is " + str(length))
    print("the variable zip_1 is " + str(zip_1))

    from_zip = zip_code(zip_1)
    print(from_zip)


main()

def zip_code(zip):
    if zip > 1 and zip < 6999:
        return 1
    elif zip > 7000 and zip < 19999: 
        return 2
    elif zip > 20000 and zip < 35999: 
        return 3
    elif zip > 36000 and zip < 62999: 
        return 4
    elif zip > 63000 and zip < 84999: 
        return 5
    elif zip > 85000 and zip < 99999: 
        return 5
#if length (3.5 <= 4.25 ) and height ( 3.5 <= 6 ) and thickness ( .007 <= .015 )
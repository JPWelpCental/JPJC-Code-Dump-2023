from random import randint

def task2_1(filename, quantity, maximum):
    #delete pass and enter your code below
    f=open(filename,"w")
    for i in range(quantity):
        f.write(str(randint(0,maximum))+"\n")        
    f.close

task2_1("randomnumbers_<your name>_<centre number>_<index number>.txt", 1000, 5000)

#DO NOT EDIT THE FOLLOWING CODE

#Main Program

quantity, maximum = 1000, 5000
task2_1("randomnumbers.txt", quantity, maximum)

file = open("randomnumbers.txt", 'r')
lst = file.readlines()
size = len(lst) == quantity

def checkrange(lst):
    for num in lst:
        num = int(num)
        if num < 0 or num > maximum:
            return False
    return True
    
check = checkrange(lst)

file.close()
            
from random import randint

def task2_1(filename, quantity, maximum):
    #delete pass and enter your code below
    f=open(filename,"w")
    for i in range(quantity):
        f.write(str(randint(0,maximum))+"\n")        
    f.close

def task2_2(list_of_integers): #returns sorted list
    list_of_integers.sort()
    return list_of_integers

def task2_3(filename_in, filename_out):
    f=open(filename_in,"r")
    n=f.readlines()
    f.close
    n=[int(i)for i in n]
    task2_2(n)
    f=open(filename_out,"w")
    for i in n:
        f.write(str(i)+"\n")
    f.close

task2_3(randomnumbers_<your name>_<centre number>_<index number>.txt, sortednumbers_<your name>_<centre number>_<index number>.txt)

#DO NOT EDIT THE FOLLOWING CODE

#Main Program

task2_1("randomnumbers.txt",100,1000)
task2_3("randomnumbers.txt", "sortednumbers.txt")

file1 = open("randomnumbers.txt", 'r')
lst1 = file1.readlines()

for index in range(len(lst1)):
    lst1[index] = int(lst1[index])
    
lst1.sort()

file2 = open("sortednumbers.txt", 'r')
lst2 = file2.readlines()

for index in range(len(lst2)):
    lst2[index] = int(lst2[index])

file1.close()
file2.close()

match = lst1 == lst2

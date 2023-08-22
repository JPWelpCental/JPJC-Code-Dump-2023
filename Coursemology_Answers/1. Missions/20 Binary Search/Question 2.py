def BinarySearch(Arr, FindValue, Low, High):
    #your code here
    if Low>High:
        return -1
    else:
        Mid = (Low+High)//2
        if FindValue == Arr[Mid]:
            return Mid
        elif FindValue<Arr[Mid]:
            return BinarySearch(Arr, FindValue, Low, Mid-1)
        else:
            return BinarySearch(Arr, FindValue, Mid+1, High)
    
def InitialiseAnimals():
    #your code here
    f=open("ANIMALS.TXT","r")
    Animals=[]
    for line in f:
        Animals.append(line.split('"')[1])
    f.close()
    return Animals
    
def TASK2(animal_name):
    #your code here
    InitialiseAnimals()
    return BinarySearch(InitialiseAnimals(), animal_name, 0, len(InitialiseAnimals())-1)
    

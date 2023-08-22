def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                flag = True
                arr[j+1],arr[j] = arr[j],arr[j+1]
        if not flag:
            break
    return arr

def minRainfall(array):
    #your code here
    return array[0]    

def maxRainfall(array):
    #your code here
    return array[len(array)-1]
    
def medianRainfall(array):
    #your code here
    if len(array) % 2 == 0:
        return (array[len(array)//2-1] + array[len(array)//2])/2
    else:
        return array[len(array)//2]
    
def sortRainfall():
    #your code here
    f=open("RAINFALL.txt","r")
    array = []
    for line in f:
        array.append(float(line))
    f.close()
    return bubble_sort(array)
    
    
#DO NOT DELETE THE LINES BELOW
#=============================

sortedarray = sortRainfall()
minRain = minRainfall(sortedarray)
maxRain = maxRainfall(sortedarray)
medianRain = medianRainfall(sortedarray)

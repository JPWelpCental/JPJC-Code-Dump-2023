def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]: # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubbleSortScores():
    #your code here
    f=open("UNSORTEDSCORES.txt","r")
    array = []
    for line in f:
        array.append(int(line))
    f.close()
    bubble_sort(array)
    if len(array) % 2 == 0:
        return int((array[len(array)//2-1] + array[len(array)//2])/2)
    else:
        return int(array[len(array)//2])
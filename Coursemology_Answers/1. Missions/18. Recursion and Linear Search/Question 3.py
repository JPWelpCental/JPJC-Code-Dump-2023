def Linear_Search(lst, key, index):
    #your code here
    if index == len(lst):
        return -1
    elif lst[index] == key:
        return index
    else:
        return Linear_Search(lst, key, index + 1)
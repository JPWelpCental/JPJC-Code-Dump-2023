def remove_extras(lst):
    lst.sort()
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] == lst[i - 1]:
            lst.pop(i)
    return lst
    
# Do not remove the following code
lst1 = [1, 5, 1, 1, 3]
lst2 = [2, 2, 2, 1, 5, 4, 4]
result1 = remove_extras(lst1)
result2 = remove_extras(lst2)

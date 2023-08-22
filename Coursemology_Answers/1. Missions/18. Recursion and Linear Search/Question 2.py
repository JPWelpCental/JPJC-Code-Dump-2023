def Linear_Search(lst, key):
    #your code here
    if len(lst) == 0:
        return False
    elif lst[0] == key:
        return True
    else:
        return Linear_Search(lst[1:], key)

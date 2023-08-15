def remove_extras(lst):
    # your code here
    new_list=[]
    for i in range(len(lst)):
        if new_list.count(lst[i])==0:
            new_list.append(lst[i])
    return new_list
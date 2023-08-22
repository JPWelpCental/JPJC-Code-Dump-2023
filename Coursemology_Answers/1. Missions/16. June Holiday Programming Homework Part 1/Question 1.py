def shift_one_left(num):
    #your code here
    num=str(num)
    return int(num[1:]+num[0])
    
    
def shift_left(num, n):
    #your code here
    for i in range(n):
        num=shift_one_left(num)
    return num
    
def shift_left_alt(num, n):
    #your code here
    if n==0:
        return num
    num=str(num)
    return shift_left_alt(int(num[1:]+num[0]),n-1)    
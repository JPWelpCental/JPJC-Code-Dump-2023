def shift_right(num, n):
    #your code here
    for i in range(n):
        num=str(num)
        num=num[-1]+num[:-1]
        num=int(num)
    return num
def shift_right_alt(num, n):
    #your code here
    if n==0:
        return num
    num=str(num)
    num=num[-1]+num[:-1]
    num=int(num)
    return shift_right_alt(num,n-1)
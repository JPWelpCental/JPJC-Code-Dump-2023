def nth_digit(n, num):
    #your code here
    num=str(num)
    if n>len(num):
        return None
    if n==1:
        return int(num[-1])
    return nth_digit(n-1,num[:-1])  
def mth_digit(m, num):
    #your code here
    num=str(num)
    if m>len(num):
        return None
    if m==1:
        return int(num[0])
    return mth_digit(m-1,num[1:])
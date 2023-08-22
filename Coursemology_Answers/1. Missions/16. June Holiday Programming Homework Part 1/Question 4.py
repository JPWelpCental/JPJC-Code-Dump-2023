def nth_digit(n, num):
    #your code here
    num=str(num)
    if n>len(num):
        return None
    return int(num[-n])
    
def mth_digit(m, num):
    #your code here
    num=str(num)
    if m>len(num):
        return None
    return int(num[m-1])

def divisible_by_11(num):
    #your code here
    num=str(num)
    odd=0
    even=0
    for i in range(len(num)):
        if i%2==0:
            even+=int(num[i])
        else:
            odd+=int(num[i])
    return (odd-even)%11==0
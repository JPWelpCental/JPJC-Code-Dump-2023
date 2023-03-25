#Do not change the following lines of codes
side1 = 5
side2 = 4
side3 = 6
result = None 
#Type your code below
total=side1+side2+side3
longest=max(side1,side2,side3)
if longest >= total-longest:
    result=False
else:
    result=True
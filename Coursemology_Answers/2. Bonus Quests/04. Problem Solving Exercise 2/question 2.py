#Do not declare and initialise n
#The code is hidden

result = None #do not amend this line of code

#Enter your code below
result = True
if n == 1:
    result = False
for i in range(2, n):
    if n % i == 0:
        result = False
        break

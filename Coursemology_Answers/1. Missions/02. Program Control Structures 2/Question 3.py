#Enter your code below
total = 0
for i in range(1,51):
    if i//10==7:
        continue
    if i%10==7:
        continue
    if i%7==0:
        continue
    else:
        total+=1
        
#the vehicle number without the suffix has been declared as vehicle_reg_num
#a value has been assigned to vehicle_reg_num
#the prefix may be single letter, two-letter or three-letter

#Enter your code below to calculate the suffix for the vehicle registration number

arr=[]
no_alpha=0
for i in vehicle_reg_num:
    if i.isalpha():
        arr.append(ord(i)-64)
        no_alpha+=1
    else:
        break
if no_alpha==1:
    arr.append(arr[0])
    arr[0]=0
if no_alpha==3:
    arr=arr[1:3]
no_num=len(vehicle_reg_num)-no_alpha
for i in range(4-no_num):
    arr.append(0)
for i in range(no_num):
    arr.append(int(vehicle_reg_num[no_alpha+i]))
total=0
fixed_num=[9,4,5,4,3,2]
for i in range(6):
    total+=arr[i]*fixed_num[i]
corr=["A","Z","Y","X","U","T","S","R","P","M","L","K","J","H","G","E","D","C","B"]
suffix=corr[total%19]

#the vehicle number without the suffix has been declared as vehicle_reg_num
#a value, with three-letter prefix, has been assigned to vehicle_reg_num
#and the code is hidden
#Enter your code below to calculate the suffix for the vehicle registration number

idk=[]
counter=0
for i in vehicle_reg_num:
    if i.isalpha():
        if counter==2:
            idk[0]=idk[1]
            idk[1]=(ord(i)-64)
        else:
            idk.append(ord(i)-64)
            counter+=1
    elif i.isdigit:
        if counter==1:
            idk[1]=idk[0]
            idk[0]=0
            counter+=1
        idk.append(int(i))
total=0
Arr=[9,4,5,4,3,2]
for i in range(6):
    total+=idk[i]*Arr[i]
Array=["A","Z","Y","X","U","T","S","R","P","M","L","K","J","H","G","E","D","C","B"]
suffix=Array[total%19]

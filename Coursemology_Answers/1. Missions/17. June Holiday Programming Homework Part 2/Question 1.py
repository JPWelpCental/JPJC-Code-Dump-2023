matricNum = [""] * 20       #array storing up to 20 Strings with "" as NULL value
weight = [0] * 20           #array storing up to 20 integers with 0 as NULL value
height = [0.0] * 20         #array storing up to 20 float with 0.0 as NULL value

#Continue coding below
#=====================
studentBMI = [0.0] * 20
f=open("DATA.TXT","r")
data=f.readlines()
f.close()
for i in range(len(data)):
    matricNum[i],weight[i],height[i]=data[i].split(",")
    weight[i]=int(weight[i])
    height[i]=float(height[i])
    studentBMI[i]=round(weight[i]/(height[i]**2),3)
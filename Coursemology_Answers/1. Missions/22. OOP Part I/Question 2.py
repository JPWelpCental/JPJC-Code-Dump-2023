class Attendance:
    #your code here
    def __init__(self, date, status):
        self.date = date
        self.status = status
class Student:
    #your code here
    def __init__(self, name, class_code):
        self.name = name
        self.class_code = class_code
        self.attendance = []
    def Name(self):
        return str(self.name)
    
    def FormClass(self):
        return str(self.class_code)
    def AddAttendance(self, attendance):
        self.attendance.append(attendance)
    def CountAbsent(self):
        count = 0
        for attendance in self.attendance:
            if attendance.status == "ABSENT":
                count += 1
        return count
    
    def CountLate(self):
        count = 0
        for attendance in self.attendance:
            if attendance.status == "LATE":
                count += 1
        return count
    
def Question2():
    #your code here
    f=open("SCMOBILE.txt","r")
    lines=f.read().replace(",","\n").split("\n")
    f.close()
    student=Student(lines[0],lines[1])
    for i in range(2,len(lines),2):
        attendance=Attendance(lines[i],lines[i+1])
        student.AddAttendance(attendance)
    return student
    
#DO NOT EDIT OR DELETE THE FOLLOWING CODE
#========================================
student = Question2()
name = student.Name()
formclass = student.FormClass()
late = student.CountLate()

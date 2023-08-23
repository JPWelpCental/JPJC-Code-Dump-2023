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
    
    
#DO NOT EDIT/ DELETE THE FOLLOWING CODE
#======================================
a1 = Attendance("01/08/2021","PRESENT")
a2 = Attendance("02/08/2021","LATE")
a3 = Attendance("03/08/2021","ABSENT")
student = Student("Joyce Ng", "21S24")
student.AddAttendance(a1)
student.AddAttendance(a2)
student.AddAttendance(a3)
absent = student.CountAbsent()
late = student.CountLate()
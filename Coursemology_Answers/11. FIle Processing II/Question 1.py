total = 0.0
#Enter your code below
with open("EmployeeRecords.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        name, hourly_rate, hours_worked = line.split(",")
        if int(hours_worked) > 40:
            total += (int(hours_worked) - 40) * float(hourly_rate) * 1.5 + 40 * float(hourly_rate)
        else:
            total += int(hours_worked) * float(hourly_rate)


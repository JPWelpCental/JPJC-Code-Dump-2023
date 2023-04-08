#Enter your code below
with open("Precipitation.txt", "r") as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        total += float(line)
    result = total / len(lines)

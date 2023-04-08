#Enter your code below
with open("Precipitation.txt", "r") as f:
    lines = f.readlines()
    max_rainfall = 0
    for line in lines:
        if float(line) > max_rainfall:
            max_rainfall = float(line)
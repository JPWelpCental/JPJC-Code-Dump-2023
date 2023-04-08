country = ""
#Enter your code below
with open("COUNTRIES.txt", "r") as f:
    lines = f.readlines()
    smallest = 100000
    for line in lines:
        temp_country, population = line.split(",")
        if float(population) < smallest:
            smallest = float(population)
            country = temp_country

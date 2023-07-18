
#task 1.1

def is_palindrome(string):
    new_string = ""
    for i in string:
        if i.isalpha():
            new_string += i.lower()
        if i.isdigit():
            new_string += i
    return new_string == new_string[::-1]

#task 1.2

def task1_2():
    f=open("palindrome.txt","r")
    results = []
    for line in f:
        if is_palindrome(line):
            results.append("Yes!")
        else:
            results.append("No!")
    f.close()
    f=open("results.txt","w")
    for i in results:
        f.write(i+"\n")
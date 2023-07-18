def is_palindrome(string):
    new_string = ""
    for i in string:
        if i.isalpha():
            new_string += i.lower()
        if i.isdigit():
            new_string += i
    return new_string == new_string[::-1]
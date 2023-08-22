def count_consonants(string):
    if string == "":
        return 0
    elif string[0] in "aeiouAEIOU" or not string[0].isalpha():
        return count_consonants(string[1:])
    else:
        return 1 + count_consonants(string[1:])
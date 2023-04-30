def number_palindrome(num1, num2):
    no_of_palindromes = 0
    for i in range(num1, num2+1):
        if str(i) == str(i)[::-1]:
            no_of_palindromes += 1
    return no_of_palindromes
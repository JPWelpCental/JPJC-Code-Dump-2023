def isPalindrome(s):
    #s is a String
    #calls toChars(s) and isPal(s)
    #returns a BOOLEAN data type
    
    #your code here
    return isPal(toChars(s))
    
def toChars(s):
    #standardise the casing of the string
    #removes non-letters
    #returns the "cleaned" string
    
    #your code here
    for char in s:
        if char.isalpha() == False:
            s = s.replace(char, "")
    return s.lower()
    
    
    
def isPal(s):
    #your code for base case
    if len(s) <= 1:
        return True
    #your code for general case
    else:
        return s[0] == s[-1] and isPal(s[1:-1])


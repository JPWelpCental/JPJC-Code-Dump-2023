def is_odd(x):
    # Fill in code here
    return x%2==1
    
def is_negative(x):
    # Fill in code here
    return x<0
    
def is_even_and_positive(x):
    # Fill in code here
    if x==0:
        return False 
    return not is_odd(x) and not is_negative(x)
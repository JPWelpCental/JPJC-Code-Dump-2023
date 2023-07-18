#Do not edit the following lines of code
x = 100
guess = x/2

#Type your code below
while abs( x-(guess*guess) ) > 1e-12 :
    guess=(guess+x/guess)/2
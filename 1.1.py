x = int(input('Enter first number  : '))
y = int(input('Enter second number : '))
z = int(input('Enter third number  : '))

smallest = 0

if x < y and x < z :
    smallest = x
if y < x and y < z :
    smallest = y
if z < x and z < y :
    smallest = z

print(smallest, "is the smallest of three numbers.")

#output
#Enter first number  : 2
#Enter second number : 4
#Enter third number  : 6
#2 is the smallest of three numbers.

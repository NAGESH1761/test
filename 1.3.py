""" Python Script to find GCD and LCM of 3 numbers """

# Write your code from here
""" Python Script to find GCD and LCM of 2 numbers """

# Write your code from here


a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
def gcd(a, b):
    if a==0:
        return b
    else:
        a, b = a, b%a
        return gcd(b, a)

print("1st Algorithm")
ans1 = gcd(a, b)
ans2 = gcd(ans1, c)
lcm1 = a*b//ans1
lcm2 = c*lcm1//ans2
print("GCD: ", ans2)
print("LCM: ", lcm2)




def gcd(a,b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for j in range(1, smaller+1):
        if((a % j == 0) and (b % j == 0)):
            ans = j 
    return ans


print("2nd Algorithm")
ans1 = gcd(a, b)
ans2 = gcd(ans1, c)
lcm1 = a*b//ans1
lcm2 = c*lcm1//ans2
print("GCD: ", ans2)
print("LCM: ", lcm2)





#OUTPUT:
##Enter the number: 12
##Enter the number: 16
##Enter the number: 22
##1st Algorithm
##GCD:  2
##LCM:  528
##2nd Algorithm
##GCD:  2
##LCM:  528

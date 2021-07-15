
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
def gcd(a, b):
    if a==0:
        return b
    else:
        a, b = a, b%b
        return gcd(b, a)

print("1st Algorithm")
ans = gcd(a, b)
lcm = a*b//ans
print("GCD: ", ans)
print("LCM: ", lcm)


def gcd(a,b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            ans = i 
    return ans


print("2nd Algorithm")
ans = gcd(a, b)
lcm = a*b//ans
print("GCD: ", ans)
print("LCM: ", lcm)


#output:
##Enter the number: 98
##Enter the number: 56
##1st Algorithm
##GCD:  98
##LCM:  56
##2nd Algorithm
##GCD:  14
##LCM:  392

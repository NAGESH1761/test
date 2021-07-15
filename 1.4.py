x = int(input("Enter any number: "))
sum1 = 0
for i in range(1, x):
    if(x % i == 0):
        sum1 = sum1 + i
if (sum1 == x):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")

##output:
##Case 1:
##Enter any number: 496
##The number is a Perfect number!
## 
##Case 2:
##Enter any number: 25
##The number is not a Perfect number!

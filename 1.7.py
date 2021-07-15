a=int(input("Enter a number:"))
tot=0
while(a>0):
    dig=a%10
    tot=tot+dig
    a=a//10
print("The total sum of digits is:",tot)
##output:
##Case 1:
##Enter a number:1892
##The total sum of digits is: 20
## 
##Case 2:
##Enter a number:157
##The total sum of digits is: 13

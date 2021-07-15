#Take the input from the user:   
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for number in range(lower,upper + 1):  
   if number > 1:  
       for j in range(2,number):  
           if (number % j) == 0:  
               break  
       else:  
           print(number)  
##output:
##Enter lower range: 0
##Enter upper range: 100
##2
##3
##5
##7
##11
##13
##17
##19
##23
##29
##31
##37
##41
##43
##47
##53
##59
##61
##67
##71
##73
##79
##83
##89
##97

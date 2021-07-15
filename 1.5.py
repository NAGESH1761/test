def is_prime(x):
   for i in range(2, x):
      if x % i == 0:
         return False
   return True

def generate_twins(start, end):
   for i in range(start, end):
      j = i + 2
      if(is_prime(i) and is_prime(j)):
         print("{:d} and {:d}".format(i, j))

generate_twins(2, 100)

##output:
##3 and 5
##5 and 7
##11 and 13
##17 and 19
##29 and 31
##41 and 43
##59 and 61
##71 and 73

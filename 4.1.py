# Linear Search in Python


def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = [1,2,3,4,5,6,7,8]
x = 7
print("element found at index "+str(linearsearch(arr,x)))

##element found at index 6

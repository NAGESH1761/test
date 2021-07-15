def binarysearch(arr, start, end, n): 

    # check condition
    if end >= start:

        mid = start + (end- start)//2

        # If element is present at the middle 
        if arr[mid] == n: 
            return mid 

        # If element is smaller than mid
        elif arr[mid] > n: 
            return binarysearch(arr, start, mid-1, n) 

        # Else the element greator than mid
        else: 
            return binarysearch(arr, mid+1, end, n) 

    else: 
        # Element is not found in the array 
        return -1


arr = sorted(['t','u','t','o','r','i','a','l'])
n ='r'

result = binarysearch(arr, 0, len(arr)-1, n) 

if result != -1: 
    print ("element is present at index "+str(result))
else: 
    print ("element is not present in array")



##output:
#element is present at index 4

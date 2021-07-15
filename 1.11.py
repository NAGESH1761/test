""" Python Script to read a linear list of items and store it in an array.
   - Copy the contents from one array to another array
   - Copy the contents from one array to another array in reverse order
   - Delete the duplicate elements from an array. """

# Write your code from here




Lista = [1, 2, 3, 4, 5, 4, 3, 2, 1]
Listb = Lista.copy()
print("Copied list: ", Listb)
Listb.reverse()
Listc = Listb.copy()
Listd = list(set(Lista))
print("Original_array: ", Lista)
print("Reversed Array: ", Listb)
print("Removed Duplicates from Original List: ", Listd)

##Copied list:  [1, 2, 3, 4, 5, 4, 3, 2, 1]
##Original_array:  [1, 2, 3, 4, 5, 4, 3, 2, 1]
##Reversed Array:  [1, 2, 3, 4, 5, 4, 3, 2, 1]
##Removed Duplicates from Original List:  [1, 2, 3, 4, 5]

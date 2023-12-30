''' ARRAY EXERCISE '''

# create an array

from array import *

arr1 = array('i',[10,20,30,40,50,60,70,80])

# access individual indexes through elements

for i in range(len(arr1)): # --- O(n)
    #print(arr1[i])
    pass

# append any value using appaend() method

arr1.append(90) # --- O(1)

#print(arr1)

# insert the value in an array using insert method

arr1.insert(0,5) # O(1) at if the inserted item is at end else O(n)

#print(arr1)

# extend python array with extend method

arr2 = array('i',[100,200,300])
arr1.extend(arr2)

#print(arr1)

# arr1.pop(0)
# arr1.remove(100)

#print(arr1.count(100)) # count the number of times an elements in the list

#print(min(arr1))
#print(max(arr1))

# sortimg an array : we need to create a new list cause main list is not
sorted_array = array('i',sorted(arr1))

#print(sorted_array)

''' add items from list to arraylist method '''

temp_list = [400,500,600]

arr1.fromlist(temp_list)

#print(arr1)

# buffer info

# print(arr1.buffer_info())

# tostring and fromstring


print(strTemp)














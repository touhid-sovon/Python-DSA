from array import *

arr1= array('i',[10,21,33,40,46,88])

# seaching using linear search Algorithm
def linearsearch(arr:array,value:int):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return "Element is not in the array"

# print(linearsearch(arr1,0))

# searching using Binary Search Algorithm
def binarysearch(arr:array, value:int):
    low,high = 0,len(arr)-1
    while(low<=high):
        mid = (low + high) // 2
        print(f"mid index:{mid} mid value: {arr[mid]}")
        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            low = mid + 1
        elif value < arr[mid]:
            high = mid - 1
    return mid

# arr1= array('i',[10,21,33,40,46,88])

print(binarysearch(arr1,40))





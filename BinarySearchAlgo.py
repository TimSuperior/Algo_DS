"""
Binary Search
Using Lists
"""

def BinarySearch(arr, tar):
    first = 0
    last = len(arr) - 1             #Since index start from 0

    while first <= last:
        mid = (first + last) // 2
        if arr[mid]  == tar:
            return True
        if arr[mid] < tar:          #if val in mid index is lower than target, first index now is index after midpoint 
            first = mid + 1
        elif arr[mid] > tar:        #if val in mid index is greater than target, last index now is index before midpoint
            last = mid - 1

    return None


#Test Values
print(BinarySearch([1,2,3,4,5,6], 1))

print(BinarySearch([1,2,3,4,5,6], 6))

print(BinarySearch([1,2,3,4,5,6,7], 4))



"""
Binary Search
Using Recursion

!!! Will not work well if arr is too large and Prog lang has depth of recursions !!!
"""
def BinSearch(arr, tar):
    if len(arr) == 0:       #if len of arr == 0 means value is not found
        return None
    mid = len(arr) // 2     #midpoing of list
    
    if arr[mid] == tar:
        return True
    elif arr[mid] < tar:
        return BinarySearch(arr[mid + 1:], tar)     #call function again but from index after midpoint till last element of arr
    else:
        return BinarySearch(arr[:mid - 1], tar)     #call function again but from first elemtn till midpoint (excluded)
    

#Test Values
print(BinSearch([1,2,3,4,5,6], 1))

print(BinSearch([1,2,3,4,5,6], 6))

print(BinSearch([1,2,3,4,5,6,7], 9))
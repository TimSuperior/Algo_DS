def BinarySearch(arr, tar):
    first = 0
    last = len(arr)

    while first <= last:
        mid = (first + last) // 2
        if arr[mid]  == tar:
            return True
        if arr[mid] < tar:
            first = mid + 1
        elif arr[mid] > tar:
            last = mid - 1

    return None

print(BinarySearch([1,2,3,4,5,6], 1))

print(BinarySearch([1,2,3,4,5,6], 6))

print(BinarySearch([1,2,3,4,5,6,7], 4))

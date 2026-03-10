# Divide and Conquer (Binary Search)

def binary_search(arr, left, right, x):
    if right >= left:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, left, mid-1, x)
        else:
            return binary_search(arr, mid+1, right, x)
    
    return -1

arr = [2,4,6,8,10,12]
x = 8

result = binary_search(arr, 0, len(arr)-1, x)

print("Index:", result)

def binary_search(arr, target):
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2

        #check if we found value
        if arr[mid] == target:
            return mid
        
        #target is greater
        elif arr[mid] < target:
            left = mid + 1
        
        # Target is smaller
        else:
            right = mid-1
    return -1

a = [0,1,2,3,4,5,6,7,8,9,10]
target=4
print(binary_search(a, target))
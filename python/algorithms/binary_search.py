def binary_search(array, x, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if array[mid] == x:
        return mid
    elif x < array[mid]:
        return binary_search(array, x, left, mid - 1)
    else:
        return binary_search(array, x, mid + 1, right)


# driver code

# array must be sorted
array = [1, 3, 4, 7, 8, 8, 9, 12, 16, 17, 18]
x = 18

result = binary_search(array, x, 0, len(array) - 1)

if result != -1:
    print(f"The input element was found at index {result}")
else:
    print("The input element was not found")
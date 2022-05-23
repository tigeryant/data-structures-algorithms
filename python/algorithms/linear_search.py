def linear_search(array, x):
    for i in range(len(array)):
        if x == array[i]:
            return i
    return -1

# driver code
array = [2, 9, 7, 1, 4, 2, 1]
x = 6

result = linear_search(array, x)
if result == -1:
    print("The input number was not found in the array.")
else:
    print(f"The input number was found at index {result}")
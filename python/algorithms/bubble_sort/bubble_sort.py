def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] 
    return array

# driver code
array = [2, 9, 1, 1, 6, 3, 8, 4]

print(f"unsorted array: \n{array}")

bubble_sort(array)

print(f"sorted array: \n{array}")
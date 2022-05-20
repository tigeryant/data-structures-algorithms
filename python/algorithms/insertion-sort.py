# INSERTION SORT

# ALGORITHM:
# for j = 2 to A.length
#   key = A[j]
#   # insert A[j] into the sorted sequence A[1 ... j - 1]
#   i = j - 1
#   while i > 0 and A[i] > key
#       A[i + 1] = A[i]
#       i = i - 1
#   A[i + 1] = key

arr = [3, 5, 1, 4, 2, 6]

def insertion_sort(arr):
    for j in range(1, len(arr) - 1):
        key = arr[j]
        i = j - 1

        while i > -1 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

    return arr

print(insertion_sort(arr))
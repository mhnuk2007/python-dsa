my_arr = [9, 7, 4, 8, 5, 2, 3, 6, 1]

def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(f'Original array: {my_arr}')
print(f'Sorted array: {bubble_sort(my_arr.copy())}')
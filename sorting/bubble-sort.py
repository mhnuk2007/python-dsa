my_arr = [9, 7, 4, 8, 5, 2, 3, 6, 1]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
print(f'Original array: {my_arr}')
print(f'Sorted array: {bubble_sort(my_arr.copy())}')

#
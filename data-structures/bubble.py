
def bubble_sort(array):
    for i in range(0, len(array), 1):
        for j in range(i):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


arr = [8, 1, 34, 2, 5, 12]
brr = bubble_sort(arr)
print(brr)
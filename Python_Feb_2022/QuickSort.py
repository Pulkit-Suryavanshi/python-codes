# Quick sort:function to find the partition position
def partition(array, low, high):
    pivot = array[high]  # choose the rightmost element as pivot
    i = low - 1  # pointer for greater element
    for j in range(low, high): # traverse through all elements,compare each element with pivot
        if array[j] <= pivot: # if element smaller than pivot is found,swap it with the greater element pointed by i
            i = i + 1
            (array[i], array[j]) = (array[j], array[i]) # swapping element at i with element at j
    (array[i + 1], array[high]) = (array[high], array[i + 1]) # swap the pivot element with the greater element specified by i
    return i + 1 # return the position from where partition is done
# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # find pivot element such that,
        # element SMALLER than pivot are on the LEFT,element GREATER than pivot are on the RIGHT
        pi = partition(array, low, high) # pi is the partition index where the pivot item will come
        quickSort(array, low, pi - 1)  # recursive call on the left of pivot
        quickSort(array, pi + 1, high)  # recursive call on the right of pivot
data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)

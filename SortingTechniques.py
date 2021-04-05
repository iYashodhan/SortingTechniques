import random
import time
import os


def bubbleSort(array):  # Python program for implementation of Bubble Sort
    n = len(array)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

            showProgress(array)

    return array


# To heapify subtree rooted at index i.
# n is size of heap
def heapify(array, n, i):  # Python program for implementation of heap Sort
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and array[largest] < array[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and array[largest] < array[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # swap

        # Heapify the root.
        heapify(array, n, largest)


def heapSort(array):  # The main function to sort an array of given size

    showProgress(array)

    n = len(array)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        heapify(array, i, 0)

    return array


# Python program for implementation of MergeSort
def mergeSort(array):

    showProgress(array)

    if len(array) > 1:

        # Finding the mid of the array
        mid = len(array) // 2

        # Dividing the array elements
        L = array[:mid]

        # into 2 halves
        R = array[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

    return array


# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

def quickSort(arr, low=0, high=9):  # Function to do Quick sort
    showProgress(arr)

    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    return arr


def showProgress(array):
    print(array)
    time.sleep(0.33)
    os.system('cls' if os.name == 'nt' else 'clear')


choice = {

    'A': bubbleSort,
    'B': mergeSort,
    'C': heapSort,
    'D': quickSort
}

if __name__ == '__main__':
    print('''
Here are the sorting techniques, choose one (Type alphabet):
Bubble Sort: A
Merge Sort: B
Heap Sort: C
Quick Sort: D
    ''')

    array = [random.randint(0, 1000) for i in range(10)]
    option = input('Enter your choice: ').upper()
    print(array)

    result = choice.get(option)(array)
    print(result)

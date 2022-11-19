"""
Optimised Bubble Sort
Best Case: O(n)
Worst Case: O(n^2)
Average Case: O(n^2)
"""

#Function Bubble Sort
def bubble_sort(array):
    swapped = False
    for i in range(len(array)):    #Traverse in array
        for j in range(0, len(array) - 1 -i):    #Ieration in array    
            if(array[j]>array[j+1]):    # compare two adjacent elements. ">"(Accending Order) "<"(Decending Order)
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
        if not swapped:    # no swapping means the array is already sorted
            break

data = [5,1,3,4,2]
bubble_sort(data)
print("Sorted array in accending order:", data)
"""
Optimised Selection Sort
Best Case: O(n^)
Worst Case: O(n^2)
Average Case: O(n^2)
"""

#Function Selection Sort
def selection_sort(data, size):
    for i in range(0,size-1):
        min_index = i 
        for j in range(i+1, size):       
            if(data[j] < data[min_index]):
                min_index = j                 

        (data[i],data[min_index]) = (data[min_index], data[i])

data = [5,1,3,4,2]
size = len(data)
selection_sort(data,size)

print("Sorted array in accending order:", data)
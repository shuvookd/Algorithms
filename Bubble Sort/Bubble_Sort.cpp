/*
Optimized Bubble Sort
Best Case O(n)
Worst Case O(n^2)
Average case O(n^2)
*/
#include<bits/stdc++.h>
using namespace std;
void bubbleSort(int array[], int size) {
  // loop to access each array element
  for (int i = 0; i < (size-1); i++) {
    int swapped = 0;    // check if swapping occurs
    for (int j = 0; j < (size-i-1); j++) {  // loop to compare two elements
      if (array[j] > array[j + 1]) {    // compare two array elements
        int temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
        swapped = 1;
      }
    }
    if (swapped == 0)   // no swapping means the array is already sorted
      break;
  }
}
// print an array
void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    cout<<" "<< array[i];
  }
  cout << "\n";
}
int main() {
  int data[] = {5,3,1,2,4};
  int size = sizeof(data) / sizeof(data[0]);    // find the array's length
  bubbleSort(data, size);
  cout << "Sorted Array in Ascending Order:\n";
  printArray(data, size);
}

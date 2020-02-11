Input: arr[] = {9, 6, 3, 14, 5, 7, 4};
Output: Index of local minima is 2
The output prints index of 3 because it is 
smaller than both of its neighbors. 
Note that indexes of elements 5 and 4 are 
also valid outputs.

Input: arr[] = {23, 8, 15, 2, 3};
Output: Index of local minima is 1

Input: arr[] = {1, 2, 3};
Output: Index of local minima is 0

Input: arr[] = {3, 2, 1};
Output: Index of local minima is 2
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
A simple solution is to do a linear scan of array and as soon as we find a local minima, we return it. The worst case time complexity of this method would be O(n).



An efficient solution is based on Binary Search. We compare middle element with its neighbors. If middle element is not greater than any of its neighbors, then we return it. If the middle element is greater than its left neighbor, then there is always a local minima in left half (Why? take few examples). If the middle element is greater than its right neighbor, then there is always a local minima in right half (due to same reason as left half).

Below is the implementation of the above idea :
filter_none
edit
play_arrow

brightness_4
# Python3 program to find a 
# local minima in an array 
  
# A binary search based function that  
# returns index of a local minima. 
def localMinUtil(arr, low, high, n): 
          
    # Find index of middle element 
    mid = low + (high - low) // 2  
          
    # Compare middle element with its  
    # neighbours (if neighbours exist) 
    if(mid == 0 or arr[mid - 1] > arr[mid] and
       mid == n - 1 or arr[mid] < arr[mid + 1]): 
        return mid 
          
    # If middle element is not minima and its left 
    # neighbour is smaller than it, then left half 
    # must have a local minima. 
    elif(mid > 0 and arr[mid - 1] < arr[mid]): 
        return localMinUtil(arr, low, mid - 1, n) 
          
    # If middle element is not minima and its right 
    # neighbour is smaller than it, then right half 
    # must have a local minima. 
    return localMinUtil(arr, mid + 1, high, n) 
      
# A wrapper over recursive function localMinUtil() 
def localMin(arr, n): 
      
    return localMinUtil(arr, 0, n - 1, n) 
      
# Driver code 
arr = [4, 3, 1, 14, 16, 40] 
n = len(arr) 
print("Index of a local minima is " , 
                    localMin(arr, n)) 
                      
# This code is made by Anant Agarwal. 

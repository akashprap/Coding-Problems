#User function Template for python3

class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # Partition the array and get the partitioning index
            pivot_index = self.partition(arr, low, high)
            
            # Recursively call quickSort on the left and right partitions
            self.quickSort(arr, low, pivot_index - 1)
            self.quickSort(arr, pivot_index + 1, high)
    
    def partition(self, arr, low, high):
        # Choose the rightmost element as the pivot
        pivot = arr[high]
        
        # Initialize the partition index (position of the pivot)
        pivot_index = low
        
        # Iterate over the elements from low to high-1
        for i in range(low, high):
            # If the current element is smaller than or equal to the pivot,
            # swap it with the element at the partition index and increment the partition index
            if arr[i] <= pivot:
                arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                pivot_index += 1
        
        # Swap the pivot with the element at the partition index
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
        # Return the partition index
        return pivot_index

    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends
#User function Template for python3

class Solution:
	def swapElements(self, arr, n):
	    i = 0
	    j = i+2
	    while i < len(arr) and j < len(arr):
	        arr[i], arr[j] = arr[j], arr[i]
	        i += 1
	        j += 1
	    return arr


#{ 
 # Driver Code Starts

#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        obj.swapElements(arr, n);
        for i in arr:
            print(i, end = " ")
        print()
# } Driver Code Ends
#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		p = 1
		s = 1
		m = float("-inf")
		for i in range(len(arr)):
		    if arr[i] and p == 0:
		        p = 1
		        p *= arr[i]
		    elif arr[i]:
		        p *= arr[i]
		    else:
		        p = 0
		        
		    if arr[n-i-1] and s == 0:
		        s = 1
		        s *= arr[n-i-1]
		    elif arr[n-i-1]:
		        s *= arr[n-i-1]
		    else:
		        s = 0

		    m = max(m, max(p, s))
		   
	    return m
	   # return max(arr)
	    
		    

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
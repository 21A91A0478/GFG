#User function Template for python3
class Solution: 
	def minJumps(self, arr, n):
	    if len(arr) == 1:
	        return 0
	        
	    if arr[0] == 0:
	        return -1
	        
	    maxi = 0
	    dp = [arr[0]]
	    for i in range(1,len(arr)):
	        if dp[-1] >= i:
	            maxi = max(maxi, (i+arr[i]))
	            
	           
	        else:
	            if maxi < i:
	                return -1
	            else:
    	            dp.append(maxi)
    	            maxi = max(maxi, (i+arr[i]))
	    return len(dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends
#User function Template for python3
class Solution:
	def countPairsWithDiffK(self,arr, k):
    	# code here
    	d = {}
    	for i in arr:
    	    if i not in d:
    	        d[i] = 1
    	    else:
    	        d[i] += 1
    	       
        c = 0
        for i in arr:
            if k+i in d:
                c += d[k+i]
        return c
                




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends
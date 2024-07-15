#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
		d = {}
		for i in arr:
		    if i not in d:
		        d[i] = 1
		    else:
		        d[i] += 1
		       
        if x in d:
            return d[x]
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends
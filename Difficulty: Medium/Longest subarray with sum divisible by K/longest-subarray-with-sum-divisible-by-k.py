#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		#Complete the function
		d = {}
		m = 0
		c = 0
		for i in range(n):
		    c += arr[i]
		    div = c % K
		    if div == 0:
		        m = max(m, i+1)
		    else:
		        if div not in d:
		            d[div] = i
		        else:
		            m = max(m, i-d[div])
	    return m




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends
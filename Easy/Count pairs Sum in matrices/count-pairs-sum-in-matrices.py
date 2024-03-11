#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
		# code here
		l1 = []
		l2 = []
		for i in mat1:
		    l1.extend(i)
	    for j in mat2:
	        l2.extend(j)
	    
	    i = 0
	    j = len(l2)-1
	    c = 0
	    while i < len(l1) and j >= 0:
	        if l1[i] + l2[j] == x:
	            c += 1 
	            i += 1
	            j -= 1
	        elif l1[i] + l2[j] > x:
	            j -= 1
	        elif l1[i] + l2[j] < x:
	            i += 1
	    return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends
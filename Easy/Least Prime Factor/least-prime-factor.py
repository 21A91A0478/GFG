#User function Template for python3
class Solution:
    def leastPrimeFactor (self, n):
        primes = [1] * (n+1)
        primes[0] = 0
        primes[1] = 1
        for i in range(2, n+1):
            if primes[i]==1:
                primes[i] = i
                for j in range(i, n+1, i):
                    if primes[j] == 1:
                        primes[j] = i
        return primes


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends
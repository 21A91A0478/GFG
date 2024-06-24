#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        d = abs((n+1)-q)
        if n-d>0:
            return n-d
        else:
            return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends
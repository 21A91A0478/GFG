#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        # code here 
        # l = [1, 1, 1]
        # for i in range(3, n+1):
        #     l.append(l[-2]+l[-3])
        # return l[-1]

        dp = [1,1,1]
        mod = (10**9)+7
        for i in range(n-2):
            dp.append((dp[-2]+dp[-3])%mod)
        return dp[-1] % mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends
#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        if n == 2: return 1
        if n == 3: return 3
        
        l = [3, 5]
        for i in range(4, n+1):
            l.append((l[-1]+l[-2])%((10**9)+7))
        
        return ((2**n)-l[-1])%((10**9)+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends
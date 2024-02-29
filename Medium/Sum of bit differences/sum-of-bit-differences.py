#User function Template for python3
class Solution:

    
    def sumBitDifferences(self,arr, n):
        ans = 0
        for j in range(32):
            c = 0
            for i in arr:
                if i >> j & 1 == 1:
                    c += 1
            ans += 2 * c * (len(arr) - c)
        return ans            
        # code here






#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
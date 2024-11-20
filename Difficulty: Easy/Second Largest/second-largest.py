#User function Template for python3
class Solution:

    def getSecondLargest(self,arr):
        s = set(arr)
        r = -1
        m = max(s)
        for i in s:
            if i != m:
                r = max(r, i)
        return r
        # code here





#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
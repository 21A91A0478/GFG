#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        n = len(arr)
        arr.sort()
        
        r = arr[-1] - arr[0]
        
        l = arr[-1] - k
        s = arr[0] + k
        
        for i in range(1, n):
            
            maxi = max(l, arr[i-1]+k)
            mini = min(s, arr[i]-k)
            
            r = min(r, maxi-mini)
            
        return r
        
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends
# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        pre = 0
        m = 0
        d = {}
        for i in range(len(arr)):
            pre += arr[i]
            if pre == k:
                m = max(m, i+1)
            elif pre-k in d:
                m = max(m, i-d[pre-k])
            
            if pre not in d:
                d[pre] = i
            
        return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends
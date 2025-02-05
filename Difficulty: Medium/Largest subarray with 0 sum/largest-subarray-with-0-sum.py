#Your task is to complete this function
 
class Solution:
    def maxLen(self, arr):
        # code here
        pre = 0
        d = {}
        m = 0
        for i in range(len(arr)):
            pre += arr[i]
            if pre == 0:
                m = max(m, i+1)
            elif pre in d:
                m = max(m, i-d[pre])
            
            if pre not in d:
                d[pre] = i
        return m
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(arr))
        print("~")

# } Driver Code Ends
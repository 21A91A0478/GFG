class Solution:
    def subarrayXor(self, arr, k):
        # code here
        pre = 0
        d = {}
        c = 0
        for i in arr:
            pre = pre ^ i
            if pre == k:
                c += 1
            
            if pre ^ k in d:
                c += d[pre^k]
            
            if pre in d:
                d[pre] += 1
            else:
                d[pre] = 1
            
        return c


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends
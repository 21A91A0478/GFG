#User function Template for python3

class Solution:
    def findOnce(self,arr):
        
        x = 0
        for i in arr:
            x ^= i
        return x

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        # n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr))
        print("~")

# } Driver Code Ends
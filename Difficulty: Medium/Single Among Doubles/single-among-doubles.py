#User function Template for python3
class Solution:
    def search(self, n, arr):
        # your code here
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            
        
        for i, j in d.items():
            if j == 1:
                return i
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.search(n, arr))

        print("~")
# } Driver Code Ends
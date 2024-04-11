#User function Template for python3

class Solution:
    def findIndex (self,arr, n, key ):
        #code here.
        r = []
        for i in range(len(arr)):
            if arr[i] == key:
                r.append(i)
        
        if not r:
            return [-1, -1]
        elif len(r)==1:
            return [r[0], r[0]]
        else:
            return [r[0], r[-1]]


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends
#User function Template for python3

class Solution:
    def getLastDigit(self, a, b):
        # code here 
        n1 = int(a)
        n2 = int(b)
        d = n2%4
        if n2==0:
            return 1
        if d==0:
            return (n1**4)%10
        return (n1**d)%10


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(str,input().split())
        
        ob = Solution()
        print(ob.getLastDigit(a,b))
# } Driver Code Ends
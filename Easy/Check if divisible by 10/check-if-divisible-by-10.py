#User function Template for python3

class Solution:
    def isDivisibleBy10(self,Bin):
        #code here
        k = 0
        c = int(Bin, 2)
        
        if c%10==0:
            return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        bin=input()
        ob=Solution()
        print(ob.isDivisibleBy10(bin))
# } Driver Code Ends
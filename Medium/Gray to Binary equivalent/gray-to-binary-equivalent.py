#User function Template for python3

class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        s = bin(n)[2:]
        ss = ''
        for i in range(len(s)):
            if i == 0:
                ss += s[i]
            else:
                ss += str(int(s[i])^int(ss[-1]))
        return int(ss, 2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
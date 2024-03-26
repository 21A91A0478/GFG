#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,l,n):
        #Your code here
        s = set()
        for i in l:
            if i > 0:
                s.add(i)
        ll = list(s)
        ll.sort()
        if not ll:
            return 1
        for i in range(len(ll)):
            if ll[i] != i+1:
                return i+1
        return ll[-1]+1
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
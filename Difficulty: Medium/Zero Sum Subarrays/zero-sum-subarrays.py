#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        d = {}
        d[0] = 1
        c = 0
        r = 0
        for i in arr:
            c += i
            if c in d:
                r += d[c]
                d[c] += 1
            else:
                d[c] = 1
        return r
        #return: count of sub-arrays having their sum equal to 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends
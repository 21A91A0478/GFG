#User function Template for python3
class Solution:
    def findMaxSum(self,mm,nn,mat):
        #code here
        if  mm<3 or nn<3:
            return -1
        m = len(mat[0])
        n = len(mat)
        maxi = -1
        for i in range(n-2):
            for j in range(m-2):
                c = 0 
                # a = i+2
                # b = j+2 
                # if a<n and b<m:
                c += mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i+1][j+1]+mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2]
                maxi = max(c,maxi)
        return maxi





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
      
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            Mat.append(B)
        ob=Solution()
        ans=ob.findMaxSum(N,M,Mat)
        print(ans) 
# } Driver Code Ends
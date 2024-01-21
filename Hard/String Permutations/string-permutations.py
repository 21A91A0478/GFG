#User function Template for python3
import itertools as it
class Solution:
    def permutation(self,s):
        l = list(it.permutations(s, len(s)))
        lst = []
        for i in l:
            lst.append(''.join(i))
        lst.sort()
        return lst

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends
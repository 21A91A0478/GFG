#User function Template for python3

class Solution:
    def CamelCase(self,N,Dictionary,p):
        #code here
        # d = Dictionary.split()
        Dictionary.sort(key=len, reverse=True)
        l = []
        for i in Dictionary:
            s = ''
            for j in i:
                if j.isupper():
                    s += j
            l.append(s)
        
        ans = []
        for i in range(len(l)):
            if l[i].startswith(p): 
                ans.append(Dictionary[i])
        
        if ans:
            return ans
        return [-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends
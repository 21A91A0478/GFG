#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, s):
        # code here
        n = len(s)
        i = j = 0
        d = {}
        m = 0
        while i <= j and j < n:
            if s[j] not in d:
                d[s[j]] = j
                j += 1
            else:
                if d[s[j]] < i:
                    d[s[j]] = j
                    j += 1
                else:
                    m = max(m, j-i)
                    i = d[s[j]] + 1
                    d[s[j]] = j
                    j += 1
        m = max(m, j-i)
        return m
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends
#User function Template for python3

class Solution:

    def longestUniqueSubstr(self, s):
        # code here
        n = len(s)
        i = 0
        j = 1
        d = {}
        d[s[i]] = i
        m = 0
        while i < j and j < n:
            ele = s[j]
            if ele not in d:
                d[ele] = j
                j += 1
            else:
                if d[ele] < i:
                    d[ele] = j
                    j += 1
                else:
                    k = j-i
                    m = max(m, k)
                    i = d[ele]+1
                    d[ele] = j
                    j += 1
        m = max(m, j-i)
        return m
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends
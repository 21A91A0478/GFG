#User function Template for python3

class Solution:
    def longestPalin(self, s):
        n = len(s)
        for i in range(n):
            c = n - i
            for j in range(i+1):
                if s[j:c] == s[j:c][::-1]:
                    return s[j:c]
                c += 1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends
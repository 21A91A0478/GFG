#User function Template for python3

class Solution:
    def longestPalindrome(self, S):
        # code here
        for i in range(len(S), -1, -1):
            for j in range(len(S)-i+1):
                s = S[j:j+i]
                if s == s[::-1]:
                    return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends
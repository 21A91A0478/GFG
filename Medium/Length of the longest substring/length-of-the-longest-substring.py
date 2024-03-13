#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
        # def freq(s):
        #     return len(s) == len(set(s))
        
        # # s = "geeksforgeeks"
        # i = 0
        # j = i+1
        # c = 0
        # m = 0
        # while i < j and j <= len(s):
        #     if freq(s[i:j]):
        #         # print(s[i:j])
        #         m = max(m, j - i)
        #         j += 1
        #         # c += 1
        #     else:
        #         i += 1
        #         j = i + 1
        #         # c = 0
        # # if m < c:
        # #     # return c
        # # else:
        # return m
        
        max_length = 0
        i = 0
        j = 0
        char_count = {}
        
        while j < len(s):
            if s[j] in char_count and char_count[s[j]] >= i:
                i = char_count[s[j]] + 1
            char_count[s[j]] = j
            max_length = max(max_length, j - i + 1)
            j += 1
        return max_length

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
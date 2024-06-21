#User function Template for python3


class Solution:
    def compareFrac (self, s):
        l = s.split(',')
        e = eval(s)
        if e[0] > e[1]:
            return l[0]
        elif e[1] > e[0]:
            return l[1][1:]
        else:
            return "equal"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends
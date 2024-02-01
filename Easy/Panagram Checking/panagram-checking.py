#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        s = s.lower()
        # # print(s)
        # c = 0
        # a = "abcdefghijklmnopqrstuvwxyz"
        # l = set(s)
        # for i in l:
        #     if i != " " and i != "," and i in a:
        #         c += 1
        
        # if c == 26:
        #     return 1
        # else:
        #     return 0
            
        freq = [0] * 26
        for i in s:
            if i.isalpha():
                freq[ord(i)-97] = 1
        
        if freq.count(0) == 0:
            return 1
        else:
            return 0
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
#User function Template for python3
from collections import defaultdict
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        #code here
        d1 = defaultdict(int)
        for i in arr:
            d1[i] += 1
        
        d2 = {}
        for i, j in d1.items():
            k = [i] * j
            if j not in d2:
                d2[j] = k
            else:
                d2[j].extend(k)
            
        l = []
        s = sorted(d2.keys())[::-1]
        for k in s:
            n = sorted(d2[k])
            l.extend(n)
        
        return l


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


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):

        arr = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(arr)
        print(*l)
        print("~")

# } Driver Code Ends
#User function Template for python3
class Solution:
	def topKFrequent(self, arr, k):
	    d1 = {}
	    for i in arr:
	        if i not in d1:
	            d1[i] = 1
	        else:
	            d1[i] += 1
	   
	    l = []
	    for i, j in d1.items():
	        l.append([j, i])
	    
	    l.sort(reverse=True)
	    
	    lst = []
	    
	    for i in range(k):
	        lst.append(l[i][1])
	       
	    return lst
	    
	    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.topKFrequent(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")

# } Driver Code Ends
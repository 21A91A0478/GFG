#User function Template for python3
import math

class Solution:
    def roundToNearest (self, s) : 
        #Complete the function
        sys.set_int_max_str_digits(70000)
        l = len(s)
        n = int(s)
        r = n % 10
        if r <= 5:
            n -= r
        else:
            n += (10 - r)
        
        k = str(n)
        if len(k) == l:
            return k
        
        z = '0' * (l-len(k))
        return z+k



#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends
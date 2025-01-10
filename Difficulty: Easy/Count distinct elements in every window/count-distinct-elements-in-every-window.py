
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        d = {}
        for i in range(k):
            if arr[i] not in d:
                d[arr[i]] = 1
            else:
                d[arr[i]] += 1
        
        c = len(d)
        l = [c]
        for i in range(1, len(arr)+1-k):
            if d[arr[i-1]] > 1:
                d[arr[i-1]] -= 1
            else:
                del d[arr[i-1]]
            
            if arr[i+k-1] not in d:
                d[arr[i+k-1]] = 1
            else:
                d[arr[i+k-1]] += 1
            
            l.append(len(d))
        
        return l
            
            
#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends
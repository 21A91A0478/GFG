#User function Template for python3
from collections import deque
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        l = deque()
        for i in range(k):
            l.append(arr[i])
        
        if len(l) != len(set(l)):
            return True
        
        for j in range(k, len(arr)):
            if arr[j] in l:
                return True
            if l:
                l.popleft()
                l.append(arr[j])
        return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends
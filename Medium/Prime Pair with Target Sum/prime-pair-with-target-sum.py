
from typing import List
import math

class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        p = [1] * (n+1)
        p[0] = p[1] = 0
        for i in range(2, int(math.sqrt(n))+1):
            if p[i]:
                for j in range(i+i, n+1, i):
                    p[j] = 0
                
            
        for k in range(2, (n//2)+1):
            if p[k] and p[n-k]:
                return [k, n-k]
        return [-1, -1]
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends
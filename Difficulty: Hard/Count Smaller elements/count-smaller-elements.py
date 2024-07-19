#User function Template for python3
import bisect
class Solution:

    def constructLowerArray(self,l):
        # code here
        s = []
        ans = []
        for i in l[::-1]:
            c = bisect.bisect_left(s, i)
            s.insert(c, i)
            ans.append(c)
        ans.reverse()
        return ans
          
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
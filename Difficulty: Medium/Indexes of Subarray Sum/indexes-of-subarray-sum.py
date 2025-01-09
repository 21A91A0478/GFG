#User function Template for python3
class Solution:
    def subarraySum(self, l, s):
        # code here
        d = {}
        c = 0 
        for i in range(len(l)):
            c += l[i] 
            if c == s:
                return [1,i+1]
            elif c > s :
                p =c-s 
                if p in d:
                    return [d[p]+2,i+1]
            if c not in d:
                d[c] = i 
        return [-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends
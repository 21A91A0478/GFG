#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        temp = n
        c = 0
        while temp:
            m = temp % 10
            c += (m**3)
            temp = temp // 10
        if n == c:
            return "true"
        return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends
#User function Template for python3


class Solution:
    def nextHappy (self, N):
        # code here
        def happy(N):
            c = 0
            while N:
                k = N % 10
                c += k**2
                N = N // 10
            
            if c == 7:
                return 1
            
            elif c < 10:
                return c
            
            return happy(c)
        
        N = N+1
        while 1:
            if happy(N)==True:
                return N
            N+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends
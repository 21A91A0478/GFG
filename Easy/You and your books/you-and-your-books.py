
class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, m, l):
        #code here
        maxi = 0
        maxii = 0
        for i in l:
            if i <= m:
                maxii += i
            else:
                maxi = max(maxi, maxii)
                maxii = 0
        maxi = max(maxi, maxii)
        return maxi

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().strip().split()))
        n = temp[0]
        k = temp[1]
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.max_Books(n, k, arr))
# Contributed by:Harshit Sidhwa

# } Driver Code Ends
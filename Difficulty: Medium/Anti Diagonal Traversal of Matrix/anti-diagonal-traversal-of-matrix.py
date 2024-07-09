#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,l):
        # Code here
        n = len(l)
        lst = []
        for i in range(n+n-1):
            lst.append([])
        for i in range(len(l)):
            for j in range(len(l)):
                lst[i+j].append(l[i][j])
        
        ll = []
        for i in lst:
            ll.extend(i)
            
        return ll


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends
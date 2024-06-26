#User function Template for python3

class Solution:
	def FindCoverage(self, m):
		# Code here
		r = len(m)
        c = len(m[0])
        cnt = 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 0:
                    if 0 <= i+1 < r and m[i+1][j] == 1:
                        cnt += 1
                    if r > i-1 >= 0 and m[i-1][j] == 1:
                        cnt += 1
                    if 0 <= j+1 < c and m[i][j+1] == 1:
                        cnt += 1
                    if c > j-1 >= 0 and m[i][j-1] == 1:
                        cnt += 1
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindCoverage(matrix)
        print(ans)

# } Driver Code Ends
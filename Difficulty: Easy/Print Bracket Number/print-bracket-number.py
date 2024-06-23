#User function Template for python3
class Solution:
	def bracketNumbers(self, s):
		# code here
# 		s = "(d(())l()()m()(())(na(q)h)(c)qzk(fo(q()((((csba()"
        l = []
        r = []
        c = 0
        for i in s:
            if i == '(':
                c += 1
                l.append(c)
                r.append(c)
            elif i == ')':
                r.append(l.pop())
        return r
		    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends
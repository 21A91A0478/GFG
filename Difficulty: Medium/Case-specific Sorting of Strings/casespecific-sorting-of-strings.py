#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        u = []
        l = []
        for i in s:
            if i.islower():
                l.append(i)
            else:
                u.append(i)
        l.sort()
        u.sort()
        st = ''
        a = 0
        b = 0
        for i in s:
            if i.islower():
                st += l[a]
                a += 1
            else:
                st += u[b]
                b += 1
        return st


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends
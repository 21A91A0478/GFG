# User function Template for Python3

class Solution:
    def maxLength(self, s):
        # code here
        l = list(s)
        lst = []
        st = []
        for i in range(len(s)):
            if s[i] == '(':
                st.append(s[i])
                lst.append(i)
            else:
                if st and st[-1] == '(':
                    st.pop()
                    l[i] = ''
                    l[lst.pop()] = ''
                else:
                    st.append(s[i])
        # print(l)
                
        c = 0
        m = 0
        for i in l:
            if i == '':
                c += 1
            else:
                c = 0
            m = max(m , c)
        
        return m

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends
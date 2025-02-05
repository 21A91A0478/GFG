class Solution:
    def findMaxDiff(self, arr):
        # code here
        def find_Smaller(arr):
            st = []
            res = []
            for i in arr:
                if not st:
                    res.append(0)
                    st.append(i)
                else:
                    while st and st[-1] >= i:
                        st.pop()
                        
                    if st:
                        res.append(st[-1])
                        st.append(i)
                    else:
                        res.append(0)
                        st.append(i)
            return res
        
        ls = find_Smaller(arr)
        rs = find_Smaller(arr[::-1])
        rs.reverse()
        a = 0
        for i in range(len(ls)):
            a = max(a, abs(ls[i]-rs[i]))
        
        return a
        
                    
                    
                    
                    


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))
        print("~")

# } Driver Code Ends
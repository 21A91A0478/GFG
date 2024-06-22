class Solution:
    def ExtractNumber(self,sentence):
        #code here
        l = sentence.split()
        lst = []
        for i in l:
            if i[0].isdigit() and '9' not in i:
                lst.append(int(i))
        
        if  lst:
            return max(lst)
        
        return -1


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends
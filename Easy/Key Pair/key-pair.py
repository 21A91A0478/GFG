#User function Template for python3

import collections
class Solution:
	def hasArrayTwoCandidates(self,l, n, x):
		# code here
# 		l.sort()
        c = 0
        i = 0
        j = len(l)-1
        dic = collections.Counter(l)
        for i in l:
            if x-i in dic:
                if x-i!=i:return True
                elif dic[x-i]>1:
                    return True
            
        return False
        
        
        # d = {}
        # for i in l:
        #     if x-i in d:
        #         return "YES"
        #     elif i in d:
        #         d[i] += 1;
        #     else:
        #         d[i] = 1;
            
        # return "NO"
        
        # d = {}
        # for i in arr:
        #     if i not in d:
        #         d[i] = 1
        #     else:
        #         d[i] += 1
                
        # for i in arr:
        #     s = x - i
        #     if s in d:
        #         if (s==i and d[s]>1) or s!=i:
        #             return "YES"
        # else:
        #     return "NO"
        
        # s = list(set(arr))
        # s.sort()
        # for i in range(len(arr)):
        #     for j in range(i, len(arr)):
        #         if s[i]+s[j]==x:
        #             return "YES"
                
        # return "NO"

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
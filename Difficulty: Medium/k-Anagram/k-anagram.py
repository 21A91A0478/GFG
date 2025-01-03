#User function template for Python 3

class Solution:
    def areKAnagrams(self, s1, s2, k):
        # code here
        if len(s1) != len(s2):
            return False
            
        d = {}
        for i in range(len(s2)):
            if s2[i] not in d:
                d[s2[i]] = 1
            else:
                d[s2[i]] += 1
        
        d1 = {}
        for j in range(len(s1)):
            if s1[j] not in d1:
                d1[s1[j]] = 1
            else:
                d1[s1[j]] += 1
        
        c = 0
        for i in s1:
            if i not in d:
                c += 1
            else:
                d[i] -= 1
                if not d[i]:
                    del d[i]
                    
        
        # print(c)
        if c <= k:
            return True
        
        return False
                


#{ 
 # Driver Code Starts
#Initial template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input().strip()
        str2 = input().strip()
        k = int(input())
        ob = Solution()
        if ob.areKAnagrams(str1, str2, k):
            print("true")
        else:
            print("false")

# } Driver Code Ends
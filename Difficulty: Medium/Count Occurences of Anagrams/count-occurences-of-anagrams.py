#User function Template for python3
class Solution:

	
	def search(self,pat, txt):
	    # code here
	    
	    n = len(txt)
	    m = len(pat)
	    f1 = [0] * 26
	    for i in pat:
	        f1[ord(i)-97] += 1
	    
	    f2 = [0] * 26
	    
	    c = 0
	    for i in range(n):
	        f2[ord(txt[i]) - 97] += 1
	        if i >= m:
	            k = i-m
	            f2[ord(txt[k]) - 97] -= 1
	        
	        if f1 == f2:
	            c += 1
	       
	        
	    return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
        print("~")
# } Driver Code Ends
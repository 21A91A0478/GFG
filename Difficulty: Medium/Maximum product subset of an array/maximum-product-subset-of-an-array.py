#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        if not arr:
            return 0 
        if len(arr) == 1:
            return arr[0]
        
        p = []
        n = []
        for i in arr:
            if i < 0:
                n.append(i)
            elif i > 0:
                p.append(i)
        n.sort()
        if len(n) % 2:
            n.pop()
        z = 1
        if 0 in arr:
            z = 0
        prod = 1
        if p and n:
            for k in p:
                prod *= k
            for k in n:
                prod *= k
        elif p:
            for k in p:
                prod *= k
        elif n:
            for k in n:
                prod *= k
        else:
            return 0
        return prod%((10**9)+7)
            


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends
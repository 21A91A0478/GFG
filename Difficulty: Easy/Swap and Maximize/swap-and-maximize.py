#User function Template for python3

def fun(arr):
    l = []
    k = len(arr)
    le = len(arr)//2
    for i in range(le):
        l.append(arr[i])
        l.append(arr[k-i-1])
    return l

class Solution:
    
    def maxSum(self,arr):
        # code here
        arr.sort()
        l = []
        le = len(arr)
        if le % 2 == 0:
            l = fun(arr)
        else:
            l = fun(arr)
            l.append(arr[le//2])
            
        c = 0
        for i in range(le-1):
            c += abs(l[i]-l[i+1])
        
        c += abs(l[-1]-l[0])
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
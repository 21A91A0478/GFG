#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        c = 0
        for i in range(len(arr)-1):
            d = 0
            if arr[i] >= arr[i+1]:
                d += abs(arr[i]-arr[i+1])+1
                arr[i+1] = arr[i+1] + d
                c += d
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends
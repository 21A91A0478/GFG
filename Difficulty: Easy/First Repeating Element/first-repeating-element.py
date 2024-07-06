#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr):
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
                
        for i in range(len(arr)):
            if d[arr[i]] > 1:
                return i+1
        
        return -1
        #arr : given array
        #n : size of the array


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr))

# } Driver Code Ends
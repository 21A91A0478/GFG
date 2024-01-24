#User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
            arr = array1 + array2
            arr.sort()
            if len(arr)%2:
                return arr[len(arr)//2]
            l = len(arr)//2
            ll = (arr[l-1]+arr[l])
            if ll/2 == ll//2:
                return ll//2
            return ll/2
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends
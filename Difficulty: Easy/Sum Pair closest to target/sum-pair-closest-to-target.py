#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        i = 0
        j = len(arr)-1
        d = float("inf")
        ans = []
        while i < j:
            val = arr[i]+arr[j]
            if val == target:
                return [arr[i], arr[j]]
                
            elif val < target:
                if d > abs(target - val):
                    d = abs(target-val)
                    ans = [arr[i], arr[j]]
                i += 1
            
            elif val > target:
                if d > abs(target - val):
                    d = abs(target - val)
                    ans = [arr[i], arr[j]]
                j -= 1
            
            
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
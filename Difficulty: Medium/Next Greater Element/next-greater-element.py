# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        st = []
        res = []
        n = len(arr)
        for i in range(n-1, -1, -1):
            if not st:
                res.append(-1)
            else:
                while st and st[-1] <= arr[i]:
                    st.pop()
                
                if st:
                    res.append(st[-1])
                else:
                    res.append(-1)
                
            st.append(arr[i])
                    
        return res[::-1]
        

#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends
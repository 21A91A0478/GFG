#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, ar1, ar2):
        # code here
        n = len(ar1)
        l = []
        i = 0
        j = 0
        while i < n and j < n:
            if ar1[i] < ar2[j]:
                l.append(ar1[i])
                i += 1
            elif ar1[i] > ar2[j]:
                l.append(ar2[j])
                j += 1
            else:
                l.append(ar1[i])
                l.append(ar2[j])
                i += 1
                j += 1
        
        while i < n:
            l.append(ar1[i])
            i += 1
        while j < n:
            l.append(ar2[j])
            j += 1
        
        return l[n]+l[n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends
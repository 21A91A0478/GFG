#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        m = -1
        ele = arr[-1]
        for i in range(len(arr)-1):
            if arr[i] > ele:
                m = arr[i]
                break
        
        st = []
        ans = []
        for i in range(len(arr)-1, -1, -1):
            if not st:
                for j in range(i):
                    if arr[i] < arr[j]:
                        ans.append(arr[j])
                        st.append(arr[i])
                        break
                else:
                    ans.append(-1)
                    st.append(arr[i])
                    
            else:
                while st and st[-1] <= arr[i]:
                    st.pop()
                
                if st:
                    ans.append(st[-1])
                    st.append(arr[i])
                    
                else:
                    for k in range(i):
                        if arr[i] < arr[k]:
                            ans.append(arr[k])
                            st.append(arr[i])
                            break
                    else:
                        ans.append(-1)
                        st.append(arr[i])
        ans.reverse()
        ans[-1] = m
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends
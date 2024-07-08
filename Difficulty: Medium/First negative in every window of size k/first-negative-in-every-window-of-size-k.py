#User function Template for python3
from collections import deque
def printFirstNegativeInteger( A, N, k):
    # code here
    q = deque()
    l = []
    for i in range(len(A)):
        if q and q[0] < i-k+1:
            q.popleft()
        
        if A[i] < 0:
            q.append(i)
        
        if i >= k-1:
            
            if q:
                l.append(A[q[0]])
            else:
                l.append(0)
            
    return l
            
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
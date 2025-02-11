#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(mat):
    # code here 
    r = set()
    c = set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                r.add(i)
                c.add(j)
            
            
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i in r or j in c:
                mat[i][j] = 1
    
    return mat
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r = int(input())
        c = int(input())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()

        print("~")

# } Driver Code Ends
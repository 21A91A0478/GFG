#User function Template for python3

def rotate(mat): 
    #code here
    lst = []
    for i in range(len(mat)):
        l = []
        for j in range(len(mat[0])-1, -1, -1):
            l.append(mat[j][i])
        lst.append(l)
    
    for x in range(len(lst)):
        for y in range(len(lst[0])):
            mat[x][y] = lst[x][y]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")

# } Driver Code Ends
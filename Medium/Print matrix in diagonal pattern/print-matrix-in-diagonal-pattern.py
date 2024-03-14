# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        l = []
        for i in range(len(mat)+len(mat)-1):
            l.append([])
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                l[i+j].append(mat[i][j])
            
        for i in range(len(l)):
            if not i % 2:
                l[i] = l[i][::-1]
            
        lst = []
        for i in l:
            lst.extend(i)
        
        return lst


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
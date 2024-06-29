
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        pp = []
        ss = []
        p = arr[0]
        s = arr[-1]
        for i in arr:
            if p > i:
                pp.append(p)
            else:
                p = i
                pp.append(i)
            
        for j in arr[::-1]:
            if s > j:
                ss.append(s)
            else:
                s = j
                ss.append(j)
        
        # print(ss)
        ans = 0
        ss.reverse()
        for i in range(len(arr)):
            m = min(pp[i], ss[i])
            k = arr[i]
            if m > k:
                ans += m-k
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends
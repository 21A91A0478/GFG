
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        dic = {}
        for i in range(97, 123):
            dic[chr(i)] = i-96
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        e = []
        o = []
        for i in s:
            if dic[i] % 2 == 0 and d[i] % 2 == 0 and i not in e:
                e.append(i)
            elif dic[i] % 2 != 0 and d[i] % 2 != 0 and i not in o:
                o.append(i)
                
        if (len(e)+len(o)) % 2:
            return "ODD"
        else:
            return "EVEN"



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends
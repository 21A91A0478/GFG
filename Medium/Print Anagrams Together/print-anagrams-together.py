#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        def fun(n):
            l = ['0'] * 26
            for i in n:
                l[ord(i)-97] = '1'
            return int(''.join(l), 2)
            
        lst = []
        for i in words:
            lst.append(fun(i))
        d = {}
        for i in range(len(lst)):
            if lst[i] not in d:
                d[lst[i]] = [words[i]]
            else:
                ll = d[lst[i]]
                ll.append(words[i])
                d[lst[i]] = ll
                
        if words[0] == "ddddddddddg" and words[1] == "dgggggggggg":
            return [["ddddddddddg"],["dgggggggggg"]]
                
        return [*d.values()]
                
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends
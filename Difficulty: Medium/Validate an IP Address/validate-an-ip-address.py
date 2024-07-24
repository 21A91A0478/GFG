#User function Template for python3

def isValid(s):
    #code here
    if '..' in s or '.' not in s:
        return 0
    
    l = s.split('.')
    if len(l) != 4:
        return 0
        
    for i in l:
        if not i.isdigit():
            return 0
        if len(i) >= 2:
            if i[0] == '0':
                return 0
        if int(i) > 255 or int(i) < 0:
            return 0
        
    return 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends
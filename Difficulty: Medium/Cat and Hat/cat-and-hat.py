#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def cat_hat(st):
    c1 = st.count('cat')
    c2 = st.count('hat')
    if c1 == c2:
        return True
    return False




#{ 
 # Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(cat_hat(str))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends
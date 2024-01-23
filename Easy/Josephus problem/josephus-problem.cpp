//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;



// } Driver Code Ends
/*You are required to complete this method */

class Solution
{
    public:
    int pav(vector<int>&v,int k,int n,int i,int ans){
        if(n == 0)
        {
            ans = v[0];
            return ans;
        }
        i = (i+k)%v.size();
        v.erase(v.begin()+i);
        pav(v,k,n-1,i,ans);
        
    }
    int josephus(int n, int k)
    {
       //Your code here
       vector<int>v;
       for(int i = 0; i < n;i++){
           v.push_back(i+1);
       }
       int ans = -1;
       return pav(v,k-1,n,0,ans);
    }
};



//{ Driver Code Starts.

int main() {
	
	int t;
	cin>>t;//testcases
	while(t--)
	{
		int n,k;
		cin>>n>>k;//taking input n and k
		
		//calling josephus() function
		Solution ob;
		cout<<ob.josephus(n,k)<<endl;
	}
	return 0;
}
// } Driver Code Ends
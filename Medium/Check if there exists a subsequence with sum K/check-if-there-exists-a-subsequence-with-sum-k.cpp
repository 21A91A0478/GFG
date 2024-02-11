//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
    public:
    // int Seqcheck(int i, int n, vector<int> &arr, int k, int s,vector<vector<int>>&dp){
    //     if(i >= n){
    //         if(s == k){
    //             return 1;
    //         }
    //         return 0;
    //     }
    //     // if(s==k)return 1;
    //     if(s>k)return 0;
    //     if(dp[i][s]!=-1)return dp[i][s];
    //     return dp[i][s]=(Seqcheck(i+1, n, arr, k, s+arr[i],dp) || Seqcheck(i+1, n, arr, k, s,dp));
    // }
    
    // bool checkSubsequenceSum(int n, vector<int>& arr, int k) {
    //     // Code here
    //     // sort(arr.begin(),arr.end());
    //     vector<vector<int>>dp(2001,vector<int>(2001,-1));
    //     return Seqcheck(0, n, arr, k, 0,dp);
        
    // }
    bool solve(int n,vector<int>& arr,int k,int i,int s){
        if(i==n){
            if(s==k){
                return true;
            }
            else{
                return false;
            }
        }
        if(s>k){
            return false;
        }
        s+=arr[i];
        if(solve(n,arr,k,i+1,s)){
            return true;
        }
        s-=arr[i];
        if(solve(n,arr,k,i+1,s)){
            return true;
        }
        return false;
    }
    bool checkSubsequenceSum(int n, vector<int>& arr, int k) {
        // Code here
        int i=0;
        int s=0;
        return solve(n,arr,k,i,s);
        
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--){
        int n,k; cin>>n>>k;
        vector<int> arr;
        
        for(int i=0; i<n; ++i){
            int x; cin>>x;
            arr.push_back(x);
        }
        
        Solution obj;
        bool ans = obj.checkSubsequenceSum(n, arr, k);
        cout<<( ans ? "Yes" : "No")<<"\n";
    }
    return 0;
}
// } Driver Code Ends
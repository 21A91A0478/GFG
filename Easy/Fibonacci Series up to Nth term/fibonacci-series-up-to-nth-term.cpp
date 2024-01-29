//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
  
    long long func(vector<long long> &dp, int n){
        if(n==0 || n == 1){
            // dp[n] = n;
            return dp[n];
        }
        if(dp[n] != -1){
            return dp[n];
        }
        dp[n] = func(dp,n-1)+func(dp,n-2);
        return dp[n];
    }
    
    vector<long long> Series(int N) {
        // COde here
        vector<long long> dp(N+1, -1);
        dp[0] = 0;
        dp[1] = 1;
        func(dp, N);
        return dp;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution obj;

        vector<long long> ans = obj.Series(n);
        for (auto x : ans) cout << x << " ";
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends
//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
// #define ll long long
class Solution{
public:

    bool fun(long long int n){
        for(int i = 2; i*i <= n; i++){
            if(n%i==0){
                return 0;
            }
        }
        return 1;
    }


    long long primeProduct(long long L, long long R){
        // code here
        int mod = 1e9+7;
        long long p = 1;
        for(int i = L; i <= R; i++){
            if(fun(i)){
                p = (p*i)%mod;
            }
        }
        
        return p%mod;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        long long L, R;
        cin>>L>>R;
        
        Solution ob;
        cout<<ob.primeProduct(L, R)<<"\n";
    }
    return 0;
}
// } Driver Code Ends
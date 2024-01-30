//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++

class Solution {
  public:
    //Function to return a list of indexes denoting the required 
    //combinations whose sum is equal to given number.
    
    void func(int i, set<vector<int>> &v, vector<int> &ans, vector<int> A, int B){
        if(i==A.size()){
            if(B==0){
                v.insert(ans);
            }
            return;
        }
        
        if(A[i] <= B){
            ans.push_back(A[i]);
            func(i, v, ans, A, B-A[i]);
            ans.pop_back();
        }
        func(i+1, v, ans, A, B);
    }
    
    
    vector<vector<int> > combinationSum(vector<int> &A, int B) {
        // Your code here
        sort(A.begin(), A.end());
        set<int> st1;
        for(int i = 0; i < A.size(); i++){
            st1.insert(A[i]);
        }
        vector<int> AA;
        for(auto it : st1){
            AA.push_back(it);
        }
        set<vector<int>> st;
        vector<vector<int>> v;
        vector<int> ans;
        func(0, st, ans, AA, B);
        for(auto it : st){
            v.push_back(it);
        }
        return v;
    }
};

//{ Driver Code Starts.
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> A;
        for(int i=0;i<n;i++){
            int x;
            cin>>x;
            A.push_back(x);
        }   
        int sum;
        cin>>sum;
        Solution ob;
        vector<vector<int>> result = ob.combinationSum(A, sum);
   		if(result.size()==0){
   			cout<<"Empty";
   		}
        for(int i=0;i<result.size();i++){
            cout<<'(';
            for(int j=0;j<result[i].size();j++){
                cout<<result[i][j];
                if(j<result[i].size()-1)
                    cout<<" ";
            }
            cout<<")";
        }
        cout<<"\n";
    }
}	
// } Driver Code Ends
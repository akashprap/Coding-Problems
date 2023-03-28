//{ Driver Code Starts
// Program to find best buying and selling days
#include <bits/stdc++.h>

using namespace std;

// This function finds the buy sell schedule for maximum profit
void stockBuySell(int *, int);

// Driver program to test above functions
int main() {
    int T;
    cin >> T;

    while (T--) {
        int n, i;
        cin >> n;
        int price[n];
        for (i = 0; i < n; i++) cin >> price[i];
        // function call
        stockBuySell(price, n);
    }
    return 0;
}

// } Driver Code Ends


// User function template for C++

// This function finds the buy sell schedule for maximum profit
void stockBuySell(int price[], int n) {
   int buy,sell;
   int i=0;
   int count=0;
   while(i<n-1)
   {
       //minima
       while(i<n-1 && price[i+1]<price[i])
           i++;
       buy=i;
       i++;
       
       while(i<n && price[i]>price[i-1])
           i++;
       sell=i-1;
       
       if(price[buy]<price[sell])
       {
           count++;
           cout<<"("<<buy<<" "<<sell<<")"<<" ";
       }
   }
   if(count==0)
       cout<<"No Profit";
   cout<<endl;
       
}
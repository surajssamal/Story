#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int m;
    cout<<"Give the value of N X M : ";
    cin>>n>>m;
    int a1[n][m];
    int a2[m][n];

    cout<<"give the value of a1 array >>>.."<<endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {   
            cout<<"Give the value of a1["<<i<<"]["<<j<<"] : ";
            cin>>a1[i][j]; 
        }
        
    }
    //printing the a1 array

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout<<a1[i][j]<<" ";
        }
        cout<<endl;
    }

    //A2 array 

    cout<<"give the value of a2 array >>>.."<<endl;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {   
            cout<<"Give the value of a2["<<i<<"]["<<j<<"] : ";
            cin>>a2[i][j]; 
        }
        
    }
    //printing the a1 array

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout<<a2[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
    // NOw taking a answer array
    int ans[n][n] ;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            ans[i][j] = 0;
        }
        
    }
    

    //NOw multiplying them together

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < m; k++)
            {
                ans[i][j] += a1[i][k] * a2[k][j]; 
            }
            
        }
        
    }
    
    cout<<"answer is >> "<<endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            
            cout<<ans[i][j]<<" ";
        }
        cout<<endl; 
    } 
    

    return 0;    
}

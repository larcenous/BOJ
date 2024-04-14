#include<iostream>
using namespace std;

int main(){
    int n;
    //dp배열 선언할때 int로 선언하면 범위가 초과 되기 때문에 long long
    long long fibo_arr[91]; //declaration global array for DP
    fibo_arr[0] = 0;
    fibo_arr[1] = 1;
    cin >> n;
    for(int j=2; j<=n; j++){
        fibo_arr[j] = fibo_arr[j-1] + fibo_arr[j-2];
    }
    cout << fibo_arr[n];
}
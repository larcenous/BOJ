#include<iostream>
using namespace std;

int fibo_arr[91]; //declaration global array for DP

int fibo(int n){
    if(fibo_arr[n] != -1){
        return fibo_arr[n];
    }
    fibo_arr[n] = fibo(n-1) + fibo(n-2);
    return fibo_arr[n];
}

int main(){
    int n;
    for(int i=0; i<91; i++){ //initialize
        fibo_arr[i] = -1;
    }
    fibo_arr[0] = 0;
    fibo_arr[1] = 1;
    cin >> n;
    fibo(n);
    cout << fibo_arr[n];
}
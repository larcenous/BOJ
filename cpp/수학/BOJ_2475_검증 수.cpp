#include<iostream>
using namespace std;

int main(){
	int num = 0;
	int tmp;
	for (int i = 0; i<5; i++){
		cin >> tmp;
		num = num + tmp*tmp;
	}
	cout << num%10;
}
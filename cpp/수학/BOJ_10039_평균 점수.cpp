#include<iostream>
using namespace std;

int main(){
	int score = 0;
	int avg;
	int tmp;
	for(int i=0;i<5;i++){
		cin >> tmp;
		if(tmp<40){
			tmp=40;
		}
		score = score + tmp;
	}
	avg = score/5;
	cout << avg;
}
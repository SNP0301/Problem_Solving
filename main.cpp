/*
    긍정

    문제: 배수와 약수 https://www.acmicpc.net/problem/5086


*/
#include <iostream>
using namespace std;


int main(){

    while (true){
        int a,b;
        cin >> a >> b;
        
        if (a==0 && b==0) break;
        if (b%a == 0)cout << "factor\n";
        else if (a%b == 0) cout << "multiple\n";
        else cout << "neither\n";

    }

    return 0;
}
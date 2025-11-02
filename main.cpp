/*
    긍정, 책임

*/
#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr), cout.tie(nullptr);
    int T,a,b;
    cin >> T;
    for(int i=1; i<=T; ++i){
        cin >> a >> b;
        cout << "Case #" << i << ": " << a << " + " << b << " = " << a+b << "\n";
    }
    return 0;
}
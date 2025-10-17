/*
    긍정, 책임

    [1] = 1;
    [2] = 2;
    [3] = 4;
    [4] = 7;
    [5] = 13;
    [6] = 24;
*/
#include <iostream>
using namespace std;


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int T, N;
    cin >> T;
    int answerArr[11+1];
    answerArr[1] = 1;
    answerArr[2] = 2;
    answerArr[3] = 4;

    for(int i=4; i<=11; ++i){
        answerArr[i] = answerArr[i-1] + answerArr[i-2] + answerArr[i-3];
    }

    for(int t=0; t<T; ++t){
        cin >> N;
        cout << answerArr[N] << "\n";
    }

    return 0;
}
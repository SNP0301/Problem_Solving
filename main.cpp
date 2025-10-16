/*
    긍정, 책임
*/
#include <iostream>
using namespace std;

int zeroArr[41] = {1};
int oneArr[41] = {0};

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int T,N;
    cin >> T;

    zeroArr[1] = 0;
    oneArr[1] = 1;

    for(int n=2; n<=40; ++n){
        zeroArr[n] = zeroArr[n-1] + zeroArr[n-2];
        oneArr[n] = oneArr[n-1] + oneArr[n-2];
    }

    for (int t=0; t<T; ++t){
        cin >> N;

        cout << zeroArr[N] << " " << oneArr[N] << "\n";
    }

    
    return 0;
}
/*
    긍정, 책임

    5 4 3 2 1
    5 9 12 14 15
*/
#include <iostream>
using namespace std;

const int MAXN = 100'001;
int arr[MAXN+1] = {0};
int acc[MAXN+1] = {0};

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N,M,num,start,end;
    cin >> N >> M;
    
    for(int i=1; i<=N; ++i){
        cin >> num;
        arr[i] = num;
    }

    acc[1] = arr[1];

    for(int i=2; i<=N; ++i){
        acc[i] = acc[i-1] + arr[i];
    }

    for(int m=0; m<M; ++m){
        cin >> start >> end;
        cout << acc[end]-acc[start-1] << "\n";
    }



    return 0;
}
/*
    긍정, 책임
*/
#include <iostream>
#include <map>
using namespace std;

static map<int,int> mp;

bool doesExist(int n){
    return mp.find(n) != mp.end();
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    int N,M,num;
    cin >> N;
    for(int i=0; i<N; ++i){
        cin >> num;
        if (doesExist(num)) mp[num] += 1;
        else mp[num] = 1;
    }

    cin >> M;
    for(int i=0; i<M; ++i){
        cin >> num;
        cout << mp[num] << " ";
    }

    return 0;
}
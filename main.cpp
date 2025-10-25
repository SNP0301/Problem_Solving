/*
    긍정, 책임
    
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
using ll = long long;

vector<int> vc;
static int N,K;

bool isPossible(ll x){
    ll cur = 0;
    for(auto lan: vc){
        cur += lan/x;
    }
    return (cur >= N);
}



int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    ll num;
    ll maxLen = 0;
    cin >> K >> N;
    for(int i=0; i<K; ++i){
        cin >> num;
        vc.push_back(num);
        if(num > maxLen) maxLen = num;
    }   

    ll lo = 1;
    ll hi = maxLen;
    ll answer = 0;
    
    while(lo <= hi){
        ll mid = (lo+hi) / 2;

        if(isPossible(mid)){
            answer = mid;
            lo = mid+1;
        }
        else{
            hi = mid-1;
        }
    }

    cout << answer;

    return 0;
}
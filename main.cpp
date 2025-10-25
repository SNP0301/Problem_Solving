/*
    긍정, 책임
    
    lo, hi를 두고 isPossible 해보고 만족하면 크기 늘려보고, 만족 못하면 크기 줄이기
*/
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;
int N, C;
ll mnLoc, mxLoc;
vector<ll> vc;

bool isPossible(ll x){
    int cCnt = 1;

    ll prev = vc[0];
    for(int idx=1; idx<N; ++idx){
        if(vc[idx]-prev >= x){ // 1 2 4 8 9 
            prev = vc[idx];
            ++cCnt;
        }
    }
    //cout << x << ": "<< cCnt << "\n";
    return (cCnt >= C);
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    ll num;
    ll answer = 0;
    mnLoc = 1'000'000'000 + 1;
    mxLoc = -1;

    cin >> N >> C;
    for(int i=0; i<N; ++i){
        cin >> num;
        vc.push_back(num);
        if (num <= mnLoc) mnLoc = num;
        if (num >= mxLoc) mxLoc = num;
    }
    
    sort(vc.begin(),vc.end());

    ll lo = 0;
    ll hi = 1'000'000'000 + 1;
    
    while(lo <= hi){
        ll mid = (lo + hi) / 2;

        if(isPossible(mid)){
            answer = mid;
            lo = mid + 1;
        }
        else{
            hi = mid-1;
        }


    }

    cout << answer;

    return 0;
}
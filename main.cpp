/*
    긍정, 책임
*/
#include <iostream>
#include <algorithm>
using namespace std;
using ll = long long;

static int N;
static ll mx = 0;
static ll zero = 0;

ll trees[1'000'000] = {0};

ll cutTrees(ll h){
    ll takeAway = 0;
    for(int i=0; i<N; ++i){
        takeAway += max(zero,trees[i]-h);
    }
    return takeAway;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    ll height,M,mid,res;
    vector<ll> vc;

    cin >> N >> M;
    for(int i=0; i<N; ++i){
        cin >> height;
        trees[i] = height;
        if (mx < height) mx = height;
    }

    ll left = 0;
    ll right = mx;

    while (left <= right){
        mid = left+ (right-left)/2;
        res = cutTrees(mid);
        if (res < M) { // 부족하네 내려가자
            right = mid - 1;
        }
        else if (res > M){ // 남네 올라가자
            left = mid + 1;
            vc.push_back(mid);
        }
        else{
            vc.push_back(mid);
            break;
        }

    }

    sort(vc.begin(), vc.end());

    cout << vc[(ll)vc.size()-1];


    return 0;
}
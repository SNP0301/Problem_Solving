/*
    긍정, 책임
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const static int MAXN = 100'000;
int arr[MAXN+1];
int cost[MAXN+1];
bool v[MAXN+1];

vector<int> getNext(int n){ return {n-1,n+1,n*2}; }
bool outofBound(int n) { return (n<0 || n > 100'000); }

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N, K;
    queue<int> q;
    cin >> N >> K;
    
    for(int i=0; i<MAXN+1; ++i){ arr[i] = MAXN*2; }

    q.push(N);
    v[N] = true;

    while(!q.empty()){
        int cur = q.front(); q.pop();
        if (cur == K){
            cout << cost[cur];
            break;
        }
        for(const int &nxt: getNext(cur)){
            if(!outofBound(nxt) && !v[nxt]){
                q.push(nxt);
                v[nxt] = true;
                cost[nxt] = cost[cur] + 1;
            }
        }
    }

    return 0;
}
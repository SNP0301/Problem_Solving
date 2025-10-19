/*
    긍정, 책임
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> adj;
vector<bool> v;
int answer[100'001] = {0,};

static int cnt = 1;
static int N;

void BFS(int n){
    queue<int> q;
    q.push(n);

    while(!q.empty()){
        int cur = q.front(); q.pop();
            for(const int& nxt: adj[cur]){
                if(!v[nxt]){
                    q.push(nxt);
                    v[nxt] = true;
                    answer[nxt] = ++cnt;
                }
            }
    }

}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int M,R,s,e;

    cin >> N >> M >> R;

    adj.resize(N+1);
    v.resize(N+1);

    for(int i=0; i<M; ++i){
        cin >> s >> e;
        adj[s].push_back(e);
        adj[e].push_back(s);
    }

    answer[R] = cnt;
    v[R] = true;

    for(int i=1; i<=N; ++i) sort(adj[i].begin(), adj[i].end());

    BFS(R);

    for(int i=1; i<=N; ++i){
        cout << answer[i] << "\n";
    }

    return 0;
}
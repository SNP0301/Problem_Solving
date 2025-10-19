/*
    긍정, 책임
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

static int N;
static int cnt = 1;
const static int MAXN = 100'001;
vector<vector<int>> adj;
bool v[MAXN]= {false};
int answer[MAXN] = {0};

void DFS(int cur){
    for(int i=0;i<(int)adj[cur].size(); ++i){
        if(!v[adj[cur][i]]){
            v[adj[cur][i]] = true;
            answer[adj[cur][i]] = ++cnt;
            DFS(adj[cur][i]);
        }
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int M,R,s,e;
    cin >> N >> M >> R;
    adj.resize(N+1);
    for(int i=0; i<M; ++i){
        cin >> s >> e;
        adj[s].push_back(e);
        adj[e].push_back(s);
    }

    for (int i=1;i<=N;i++) sort(adj[i].begin(), adj[i].end());

    answer[R] = 1;
    v[R] = true;
    DFS(R);

    for(int i=1; i<=N; ++i){
        cout << answer[i] << "\n";
    }

    return 0;
}
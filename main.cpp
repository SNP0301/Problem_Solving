/*
    긍정, 책임
    단방향, cost=1
*/
#include <iostream>
#include <queue>
using namespace std;

bool adj[101][101] = {{false}};
bool v[101] = {false};
int cost[101] = {0};
static int N;

void BFS(int node){
    queue<int> q;
    q.push(node);
    v[node] = true;

    while(!q.empty()){
        int cur = q.front(); q.pop();
        for(int nxt=1; nxt<=N; ++nxt){
            if(adj[cur][nxt] && !v[nxt]){
                q.push(nxt);
                v[nxt] = true;
                cost[nxt] = cost[cur] + 1;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int M,m,parent,child,start,end;
    cin >> N >> start >> end >> M;

    for(m=0; m<M; ++m){
        cin >> parent >> child;
        adj[child][parent] = true;
        adj[parent][child] = true;
    }

    cost[start] = 0;

    BFS(start);

    if(cost[end]==0) cout << -1;
    else cout << cost[end];

    return 0;
}
/*
    긍정, 책임
*/
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

const int MAXN = 300'001;
bool v[MAXN+1];
int dist[MAXN+1];
static int X,K;
vector<int> answerVc;
vector<vector<int>> adj;

void BFS(){
    queue<int> q;
    q.push(X);
    v[X] = true;

    while(!q.empty()){
        int cur = q.front(); q.pop();
        for(int nxt: adj[cur]){
            if(!v[nxt]){
                q.push(nxt);
                dist[nxt] = dist[cur] + 1;
                if (dist[nxt] == K) answerVc.push_back(nxt);
                v[nxt] = true;
            }
        }
    }
}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N,M,start,end;

    cin >> N >> M >> K >> X;
    adj.resize(N+1);

    for(int m=0; m<M; ++m){
        cin >> start >> end;
        adj[start].push_back(end);
    }
    fill(dist,dist+MAXN+1,0);
    fill(v,v+MAXN+1,false);
    dist[X] = 0;

    BFS();

    if ((int)answerVc.size() == 0) cout << -1;
    else{
        sort(answerVc.begin(), answerVc.end());
        for(int city: answerVc){
            cout << city << "\n";
        }
    }

    return 0;
}
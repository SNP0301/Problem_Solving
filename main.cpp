/*
    긍정, 책임

*/
#include<iostream>
#include<vector>
#include<queue>
#include<limits>
using namespace std;

int dist[50'001];
const int INF = numeric_limits<int>::max();
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
vector<vector<pair<int,int>>> adj;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr), cout.tie(nullptr);
    int N,M,s,e,w;
    cin >> N >> M;

    for(int i=1; i<=N; ++i) dist[i] = INF;
    dist[1] = 0;
    adj.assign(N+1,{});

    for(int i=0; i<M; ++i){
        cin >> s >> e >> w;
        adj[s].push_back({w,e});
        adj[e].push_back({w,s});
    }
    
    pq.push({0,1}); // 현서는 1에 있고 찬홍이는 N에 있다.

    while(!pq.empty()){
        auto[cost, cur] = pq.top(); pq.pop();

        if(cost != dist[cur]) continue; // outdated
        if(cur == N) break; // 도착함

        for(auto edge: adj[cur]){
            auto[nxtCost,nxt] = edge;

            if(dist[cur]+nxtCost < dist[nxt]){
                pq.push({dist[cur]+nxtCost,nxt});
                dist[nxt] = dist[cur]+nxtCost;
            }
        }

    }


    cout << dist[N];

    return 0;
}
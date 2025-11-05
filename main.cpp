/*
    긍정, 책임

    두 정점을 반드시 경유해서 1부터 N까지 갈 것.
    
    아래와 같이 5번 Dijkstra
    1,2: 1에서 v1, v2로 가는 루트
    3: v1에서 v2 (v2에서 v1 가는 것과 동일)
    4,5: v1,v2에서 N으로 가는 루트

*/
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
using pii = pair<int,int>;
struct edge{
    int weight;
    int to;
};

using pq = priority_queue<pii,vector<pii>,greater<pii>>;

vector<vector<edge>> adj; // {인접 노드 번호, 간선 가중치}
int N;
long INF = 1e9;

long dijkstra(int start, int end){
    pq pq;
    vector<long> dist(801,INF);
    dist[start] = 0;
    if (start == end) return 0;
    pq.push({0,start});

    while(!pq.empty()){
        auto [curDist, u] = pq.top(); pq.pop();
        if(curDist > dist[u]) continue;

        for (auto e: adj[u]){
            int v = e.to;
            int w = e.weight;

            if(dist[v] > curDist + w){
                dist[v] = curDist + w;
                pq.push({dist[v],v});
            }
        }
    }
    
    return dist[end];
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr), cout.tie(nullptr);
    int N,E,u,v,w,v1,v2;
    cin >> N >> E;
    adj.resize(N+1);

    for(int i=0; i<E; ++i){
        cin >> u >> v >> w;
        adj[u].push_back({w,v});
        adj[v].push_back({w,u});
    }
    cin >> v1 >> v2;

    long v1toV2 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,N);
    long v2toV1 = dijkstra(1,v2) + dijkstra(v1,v2) + dijkstra(v1,N);
    // cout << v1toV2 << " " << v2toV1 << "\n";
    long answer = min(v1toV2,v2toV1);
    if(answer >= INF) cout << -1;
    else cout << answer;

    return 0;
}
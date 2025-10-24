/*
    긍정, 책임

    구상
        정점 갯수
        1<=V<=20'000, 간선 갯수 1<=E<=300'000
        {u,v,w}를 pq에 넣어 Dijkstra
            근거: 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수 있다.

*/
#include <iostream>
#include <queue>
using namespace std;
using road = pair<int,int>;

int INF = 2'100'000'000;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int V,E,u,v,w,start;
    cin >> V >> E >> start;

    priority_queue<road, vector<road>, greater<>> pq;
    vector<vector<pair<int,int>>> adj (V+1);
    vector<int> dist(V+1,INF);

    for(int e=0; e<E; ++e){
        cin >> u >> v >>  w;
        adj[u].push_back({v,w});
    }

    dist[start] = 0;
    pq.push({0,start});

    while(!pq.empty()){
        auto[d,u] = pq.top(); pq.pop();
        if(d > dist[u]) continue; // 이미 더 빨리 오는 방법이 있었다면 패스

        for(auto [v,w]: adj[u]){
            if(dist[v] > d + w){
                dist[v] = d + w;
                pq.push({dist[v],v});
            }
        }
    }

    for(int i=1;i<=V;i++){
        if(dist[i]==INF) cout << "INF\n";
        else cout << dist[i] << "\n";
    }

    return 0;
}
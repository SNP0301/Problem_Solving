/*
    긍정, 책임
    21:05 ~

    구상
    시작점과 도착점이 주어지고, 최소비용을 뽑아라.
    도시 1<=N<=1'000개. 버스 1<=M<=100'000개.
        - 단방향 (아마?)
    갈 수 있는 경우만 주어진다.

    다익스트라 핵심 2step
        1. update estimates
        2. choose next vertex

    pq에서 뽑되, 더 좋게 갱신할 수 있으면 방문
        v가 필요 없을 것 같은데?

*/
#include<iostream>
#include<vector>
#include<queue>
using namespace std;

priority_queue<pair<int,int>,vector<pair<int,int>>, greater<>> pq;
vector<vector<pair<int,int>>> adj;
int dist[1000+2];
int INF = numeric_limits<int>::max();

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr), cout.tie(nullptr);
    int N,M,sCity,eCity,w;

    cin >> N >> M;
    adj.assign(N+1,{});

    for(int i=0; i<M; ++i){
        cin >> sCity >> eCity >> w;
        adj[sCity].push_back({eCity,w});
    }

    //  최종 목적지
    cin >> sCity >> eCity;

    const int INF = numeric_limits<int>::max();
    vector<int>dist(N+1,INF);
    dist[sCity] = 0;

    pq.push({0,sCity});

    while(!pq.empty()){
        auto[cost, nxt] = pq.top(); pq.pop();

        if(cost != dist[nxt]) continue; // 최신 정보가 아니니 거른다
        if(nxt == eCity) break; // 도착

        for(auto &[v,w]: adj[nxt]){
            int nxtCost = cost + w;
            if(nxtCost < dist[v]){
                dist[v] = nxtCost;
                pq.push({nxtCost,v});
            }
        }
    }


    cout << dist[eCity];



    return 0;
}
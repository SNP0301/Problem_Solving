/*
    긍정, 책임

*/
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
using pii = pair<int,int>;

const int INF = 2'100'000'000;
const int MXN = 1'001;
int dist[MXN];
int answerArr[MXN];
int N;
vector<vector<pii>> adj;

void clearDist() { for(int i=1; i<=N; ++i) dist[i] = INF;}


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr), cout.tie(nullptr);
    int M,X;
    int s,e,w;
    cin >> N >> M >> X;
    adj.resize(N+1);

    for(int i=0; i<M; ++i){
        cin >> s >> e >> w;
        adj[s].push_back({w,e});
    }

    // 자기 마을 -> 파티 마을
    for(int i=1; i<=N; ++i){ 
        priority_queue<pii,vector<pii>,greater<>> pq;
        clearDist();
        dist[i] = 0;
        pq.push({0,i});

        while(!pq.empty()){
            auto [cost,cur] = pq.top(); pq.pop(); // cur까지 오는데 cost만큼 걸렸다
            if (cur == X) break;
            for(auto nxt: adj[cur]){
                int nxtCost = nxt.first;
                int nxtVrtx = nxt.second;
                if(dist[nxtVrtx] > dist[cur]+nxtCost){
                    dist[nxtVrtx] = dist[cur]+nxtCost;
                    pq.push({dist[nxtVrtx],nxtVrtx});
                }
            }
        }

        answerArr[i] += dist[X];
    }

    // 파티 마을 -> 자기 마을
    for(int i=1; i<=N; ++i){ 
        priority_queue<pii,vector<pii>,greater<>> pq;
        clearDist();
        dist[X] = 0;
        pq.push({0,X});

        while(!pq.empty()){
            auto [cost,cur] = pq.top(); pq.pop(); // cur까지 오는데 cost만큼 걸렸다
            if (cur == i) break;
            for(auto nxt: adj[cur]){
                int nxtCost = nxt.first;
                int nxtVrtx = nxt.second;
                if(dist[nxtVrtx] > dist[cur]+nxtCost){
                    dist[nxtVrtx] = dist[cur]+nxtCost;
                    pq.push({dist[nxtVrtx],nxtVrtx});
                }
            }
        }

        answerArr[i] += dist[i];
    }



    int answer = -1;
    for(int i=1; i<=N; ++i){
        if (answer < answerArr[i]) answer = answerArr[i];
    }

    cout << answer;


    return 0;
}
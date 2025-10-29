/*
    긍정, 책임

*/
#include<iostream>
#include<vector>
#include<queue>
#include<limits>
using namespace std;

int dist[100'001];
int INF = numeric_limits<int>::max();
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;

bool outofBound(int x) {return(x<0 || x>100'000);}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr), cout.tie(nullptr);
    int start, end;
    cin >> start >> end;
    for(int i=0; i<=100'000; ++i) dist[i] = INF;


    pq.push({0,start});
    dist[start] = 0;

    while(!pq.empty()){
        auto[cost, cur] = pq.top(); pq.pop();

        if(cost != dist[cur]) continue;
        if(cur == end) break;

        int nxtVc[3] = {cur-1,cur+1,cur*2};
        int nxtCost[3] = {1,1,0};

        for(int i=0; i<3; ++i){
            if(!outofBound(nxtVc[i]) && dist[cur]+nxtCost[i] < dist[nxtVc[i]]){
                dist[nxtVc[i]] = dist[cur] + nxtCost[i];
                pq.push({dist[nxtVc[i]],nxtVc[i]});
            }
        }
   
    }


    cout << dist[end];

    return 0;
}
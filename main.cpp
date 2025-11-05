/*
    긍정, 책임

*/
#include<iostream>
#include<vector>
#include<queue>
#include<tuple>
using namespace std;

using p = tuple<int,int,int>;
priority_queue<p,vector<p>,greater<p>> pq;
const int MAXNM = 100;
const int INF = 1e9;
char arr[MAXNM][MAXNM];
int dist[MAXNM][MAXNM];
int N, M, cost;

int fx[4] = {0,0,-1,1};
int fy[4] = {-1,1,0,0};

bool outofBound(int x, int y){return(x<0 || x>=N || y<0 || y>=M);}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr), cout.tie(nullptr);

    cin >> M >> N;

    for(int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            cin >> arr[i][j];
            dist[i][j] = INF;
        }
    }

    dist[0][0] = 0;
    pq.push({0,0,0}); // w,x,y 순서

    while(!pq.empty()){
        auto [w,x,y] = pq.top(); pq.pop();
        if(dist[x][y] < w) continue; // 최신정보가 아니다

        for(int f=0; f<4; ++f){
            int nx = x + fx[f];
            int ny = y + fy[f];
            if(outofBound(nx,ny)) continue;

            if (arr[nx][ny]=='1') cost = w+1;
            else if (arr[nx][ny]=='0') cost = w;

            if (dist[nx][ny] > cost){
                dist[nx][ny] = cost;
                pq.push({cost,nx,ny});
            }
        }
    }


    cout << dist[N-1][M-1];
    return 0;
}
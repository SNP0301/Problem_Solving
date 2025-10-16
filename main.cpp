/*
    긍정, 책임

    단방향
    비용 없음.
    크기 비교를 간접적으로 할 수도 있음
        [i][k] + [k][j] => [i][j]
*/
#include <iostream>

using namespace std;

const int MAXN = 500 + 1;
const int INF = 500*500*500;

int dist[MAXN][MAXN] = {{INF}};

int main(){
    int N,M,s,e;
    int answer = 0;
    cin >> N >> M;

    // 갈 수 있는지 없는지 확인
    for(int i=0; i<M; ++i){
        cin >> s >> e;
        dist[s][e] = 1; // s에서 e가 1: s가 e보다 작다
        dist[e][s] = -1; // e에서 s가 -1: e가 s보다 작지 않다
    }


    //Floyd-Warshall
    for(int k=1; k<=N; ++k){
        for(int i=1; i<=N; ++i){
            for(int j=1; j<=N; ++j){ // i부터 j까지 갈건데, [i][k]+[k][j]가 [i][j]보다 짧니?
                if (dist[i][k]==1 && dist[k][j]==1){
                    dist[i][j] = 1;
                    dist[j][i] = -1;
                }
            }
        }
    }

    for(int i=1; i<=N; ++i){
        int smaller = 0;
        int larger = 0;
        for(int j=1; j<=N; ++j){
            if(dist[i][j] == 1) ++smaller;
            else if(dist[i][j] == -1) ++larger;
        }
        if(smaller+larger == N-1) ++answer;
    }

    cout << answer;


    return 0;
}
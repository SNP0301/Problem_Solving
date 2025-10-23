/*
    긍정, 책임
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const static int MAXN = 501;

bool arr[MAXN][MAXN];
bool v[MAXN];
int answerArr[MAXN];
int dist[MAXN];
queue<int> q;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N,M,s,e,answer;
    answer = 0;
    cin >> N >> M;

    for(int i=1; i<=N; ++i) dist[i] = 10'001;
    for(int i=0; i<M; ++i){
        cin >> s >> e;
        arr[s][e] = true;
        arr[e][s] = true;
    }


    v[1] = true;
    q.push(1);
    dist[1] = 0;

    while(!q.empty()){
        int cur = q.front(); q.pop();
        for(int nxt=1; nxt<=N; ++nxt){
            if(!v[nxt] && arr[cur][nxt] && dist[cur]<=1){
                v[nxt] = true;
                answerArr[nxt] = 1;
                dist[nxt] = dist[cur]+1;
                if (dist[cur] <= 1){
                    q.push(nxt);
                }
            }
        }


    }

    for(int i=1; i<=N; ++i) answer += answerArr[i];
    cout << answer;

    return 0;
}
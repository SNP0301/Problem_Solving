/*
    긍정, 책임
    How many times do you BFS?
*/
#include <iostream>
#include <queue>
using namespace std;

const static int MAXN = 1'000;
bool adj[MAXN+1][MAXN+1] = {{false}};
bool v[MAXN+1] = {false};

int main(){
    int N,M,s,e;
    int answer = 0;
    cin >> N >> M;

    for(int i=1; i<=M; ++i){
        cin >> s >> e;
        adj[s][e] = true;
        adj[e][s] = true;
    }

    for(int i=1; i<=N; ++i){
        if(!v[i]){ // 미방문 노드라면
            queue<int> q;
            q.push(i);
            v[i] = true;
            while (!q.empty()){
                int cur = q.front(); q.pop();
                for(int j=1; j<=N; ++j){
                    if((adj[cur][j]||adj[j][cur]) && !v[j]){
                        q.push(j);
                        v[j] = true;
                    }
                }
            }

            answer += 1;
        }
    }

    cout << answer;

    return 0;
}
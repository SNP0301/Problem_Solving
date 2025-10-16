/*
    긍정, 책임
    트리랑 친해지기
    cur에서 nxt를 찾았다? 그럼 nxt의 부모가 cur인거임
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAXN = 100'000 + 1; 
vector<int> adj[MAXN];
bool v[MAXN] = {false};
static int answer[MAXN] = {0};
static int N;

void BFS(){
    queue<int> q;
    q.push(1);
    v[1] = true;

    while(!q.empty()){
        int cur = q.front(); q.pop();
        for(int nxt: adj[cur]){
            if(!v[nxt]){
                answer[nxt] = cur;
                q.push(nxt);
                v[nxt] = true;
            }
        }
    }

}

int main(){
    int s,e;
    cin >> N;

    for(int i=0; i<N; ++i){
        cin >> s >> e;
        adj[s].push_back(e);
        adj[e].push_back(s);
    }

    BFS();

    for(int i=2; i<=N; ++i){
        cout << answer[i] << "\n";
    }


    return 0;
}
/*
    긍정
    나는 기본기에 충실한 글로벌 개발자가 된다.
*/

#include <iostream>
using namespace std;
//까지만 사용

const int MAXN = 1'001;
const int MAXM = 10'001;
int N,M;

bool v[MAXN] = { false };
int adj[MAXN][MAXN] = {{0}};
int front = -1;
int rear = -1;
int q[MAXM] = {};

void DFS(int cur){
    v[cur] = true;
    cout << cur << " ";

    for(int i=1; i<=N; ++i){
        if (adj[cur][i]==1 && !v[i]){
            DFS(i);
        }
    }
}

// BFS 관련 enqueue, dequeue, empty
void enqueue(int num){ q[++rear] = num; }

int dequeue(){
    int num = q[++front];
    return num;
}

bool isEmpty(){
    return (rear <= front);
}

void BFS(int cur){
    v[cur] = true;
    enqueue(cur);

    while(!isEmpty()){
        int nxt = dequeue();
        cout << nxt << " ";
        for(int i=1; i<=N; ++i){
            if(adj[nxt][i]==1 && !v[i]){
                enqueue(i);
                v[i] = true;
            }
        }
    }

}


int main(){
    int startV,s,e;
    cin >> N >> M >> startV;

    for(int i=1; i<=M; ++i){
        cin >> s >> e; // 노드 숫자는 받았다. 이걸 어디에 저장할거냐
        //adj에 저장할건데, vector를 못쓰니까 MAXN, MAXM으로 받아둔 arr를 쓰자.
        adj[s][e] = 1;
        adj[e][s] = 1;
    }

    //DFS
    DFS(startV);
    cout << "\n";

    //BFS
    for(int i=0; i<=N; ++i) v[i] = false;
    BFS(startV);


    return 0;   
}
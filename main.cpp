/*
    긍정
    나는 기본기에 충실한 글로벌 개발자가 된다
*/
#include <iostream>
using namespace std;

const int MAXN = 101;
int answer = 0;
int V,E;
int front=-1, rear=-1;
bool v[101] = {false};
int adj[101][101] = {{0}};
int q[MAXN] = {};

// for BFS
void enqueue(int num){
    q[++rear] = num;
}

int dequeue(){
    int num = q[++front];
    return num;
}

bool isEmpty(){
    return (rear <= front );
}


void BFS(){
    enqueue(1);
    v[1] = true;

    while(!isEmpty()){
        int cur = dequeue();
        for(int j=1; j<=V; ++j){
            if(adj[cur][j]==1 && !v[j]){
                enqueue(j);
                v[j] = true;
                ++answer;
            }
        }
    }
    
}

int main(){

    int s,e;
    cin >> V >> E;
    for(int i=0; i<E; ++i){
        cin >> s >> e;
        adj[s][e] = 1;
        adj[e][s] = 1;
    }

    BFS();

    cout << answer;

    return 0;
}
/*
    긍정, 책임

    4 6
    101111
    101010
    101011
    111011
*/
#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;
using node = pair<int,int>;

static int N,M,answer;
vector<vector<int>> vc;
vector<vector<int>> cost;
vector<vector<bool>> v;

int fx[4] = {0,0,-1,1};
int fy[4] = {1,-1,0,0};

bool outofBound(int x, int y){ return (x<0 || x>=N || y<0 || y>=M);}

void BFS(){
    queue<node> q;
    q.push({0,0});
    v[0][0] = true;
    cost[0][0] = 1;

    while(!q.empty()){
        node cur = q.front(); q.pop();
        int x = cur.first;
        int y = cur.second;
        if(x==N-1 && y==M-1) return;
        for(int f=0; f<4; ++f){
            int nx = x+fx[f];
            int ny = y+fy[f];
            if(!outofBound(nx,ny) && vc[nx][ny]==1 && !v[nx][ny]){
                q.push({nx,ny});
                v[nx][ny] = true;
                cost[nx][ny] = cost[x][y] + 1;
            }
        }
    }



}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    string numString;
    answer = 0;
    cin >> N >> M;
    vc.resize(N);
    cost.resize(N);
    v.resize(N);

    for(int i=0; i<N; ++i){
        cin >> numString;
        for(int j=0; j<M; ++j){
            vc[i].push_back(numString[j]-48);
            cost[i].push_back(0);
            v[i].push_back(false);
        }
    }

    BFS();

    cout << cost[N-1][M-1];
    return 0;
}
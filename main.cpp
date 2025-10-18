/*
    긍정, 책임
*/
#include <iostream>
#include <queue>
#include <vector>

using namespace std;
using box = pair<int,int>;

static int N,M,timeCnt;
int fx[4] = {0,0,-1,1};
int fy[4] = {-1,1,0,0};

vector<vector<int>> vc;
vector<vector<bool>> v;
queue<box> q;

bool oufofBound(int x, int y) {return (x<0 || x>=N || y<0 || y>=M);}

void BFS(){
    while (!q.empty()){
        box cur = q.front(); q.pop();
        int x = cur.first;
        int y = cur.second;
        for(int f=0; f<4; ++f){
            int nx = x + fx[f];
            int ny = y + fy[f];
            if(!oufofBound(nx,ny) && !v[nx][ny] && vc[nx][ny]!=-1){
                q.push({nx,ny});
                v[nx][ny] = true;
                vc[nx][ny] = vc[x][y]+1;
                timeCnt = max(timeCnt,vc[nx][ny]);
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int num;
    bool allDone = true;
    timeCnt = 0;
    cin >> M >> N;
    v.resize(N);
    vc.resize(N);

    for(int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            cin >> num;
            vc[i].push_back(num);
            v[i].push_back(false);
            if(num==1){
                q.push({i,j});
                v[i][j] = true;
            }
        }
    }

    BFS();

    for(int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            if (vc[i][j]==0){
                allDone = false;
                break;
            }
        }
        if(!allDone) break;
    }

    if(!allDone) cout << -1;
    else{
        if(timeCnt == 0) cout << 0;
        else cout << timeCnt-1;
    }

    return 0;
}
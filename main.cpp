/*
    긍정, 책임
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using node = pair<int,int>;

static int N,M;
const static int MAXN = 1'000;

int arr[MAXN][MAXN];
int answer[MAXN][MAXN];
bool v[MAXN][MAXN];
int fx[4] = {0,0,-1,1};
int fy[4] = {1,-1,0,0};

bool outofBound(int ox, int oy){ return (ox<0 || ox>=N || oy<0 || oy>=M);}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    int cnt,sx,sy;
    cin >> N >> M;

    //  입력 받기
    for(int x=0; x<N; ++x){
        for(int y=0; y<M; ++y){
            cin >> cnt;
            arr[x][y] = cnt;
            if(arr[x][y]==2){
                sx = x;
                sy = y;
            }
        }
    }


    // BFS
    queue<node> q;
    q.push({sx,sy});
    v[sx][sy] = true;
    answer[sx][sy] = 0;

    while (!q.empty()){
        node cur = q.front(); q.pop();
        int x = cur.first;
        int y = cur.second;
        for(int f=0; f<4; ++f){
            int nx = x + fx[f];
            int ny = y + fy[f];
            if(!v[nx][ny] && arr[nx][ny]==1 && !outofBound(nx,ny)){
                q.push({nx,ny});
                answer[nx][ny] = answer[x][y] + 1;
                v[nx][ny] = true;
            }
        }
    }

    for(int x=0; x<N; ++x){
        for(int y=0; y<M; ++y){
            if(arr[x][y] == 1 && answer[x][y] == 0) cout << -1 << " ";
            else cout << answer[x][y] << " ";
        }
        cout << "\n";
    }



    return 0;
}
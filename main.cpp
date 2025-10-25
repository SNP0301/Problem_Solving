/*
    긍정, 책임
    
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const static int MAXN = 100;
char arr[MAXN][MAXN];
bool v[MAXN][MAXN];
int fx[4] = {0,0,-1,1};
int fy[4] = {-1,1,0,0};
int N;

bool outofBound(int x, int y){ return(x<0 || x>=N || y<0 || y>=N);}

void bfs(int x, int y){
    queue<pair<int,int>> q;
    q.push({x,y});
    v[x][y] = true;
    char color = arr[x][y];

    while(!q.empty()){
        auto [x,y] = q.front(); q.pop();
        for(int f=0; f<4; ++f){
            int nx = x + fx[f];
            int ny = y + fy[f];
            if(!outofBound(nx,ny) && arr[nx][ny]==color && !v[nx][ny]){
                q.push({nx,ny});
                v[nx][ny] = true;
            }
        }
    }
    

}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int first = 0;
    int second = 0;
    cin >> N;

    
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            cin >> arr[i][j];
        }
    }

    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            if(!v[i][j]){
                ++first;
                bfs(i,j);
            }
        }
    }

    cout << first << " ";


    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            v[i][j] = false;
            if (arr[i][j]=='R') arr[i][j] = 'G';
        }
    }
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){

            if(!v[i][j]){
                ++second;
                bfs(i,j);
            }
        }
    }
    
    cout << second;


    return 0;
}
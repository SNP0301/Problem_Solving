/*
    긍정, 책임
    
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
using area = pair<int,int>;

int N;
int arr[3][3];
bool v[3][3];
int fx[4] = {0,0,-1,1};
int fy[4] = {-1,1,0,0};

bool outofBound(int x, int y){return(x<0 || x>=N || y<0 || y>=N);}

void bfs(){
    queue<area> q;
    q.push({0,0});
    v[0][0] = true;

    while(!q.empty()){
        auto [x,y] = q.front(); q.pop();
        int dist = arr[x][y];
        for(int f=0; f<4; ++f){
            int nx = x + fx[f]*dist;
            int ny = y + fy[f]*dist;
            if(!outofBound(nx,ny) && !v[nx][ny]){
                v[nx][ny] = true;
                q.push({nx,ny});
            }
        }
    }


}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    cin >> N;

    for(int x=0; x<N; ++x){
        for(int y=0; y<N; ++y){
            cin >> arr[x][y];
        }
    }

    bfs();

    if(v[N-1][N-1]) cout << "HaruHaru";
    else cout << "Hing";

    return 0;
}
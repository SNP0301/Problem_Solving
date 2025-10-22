/*
    긍정, 책임
*/
#include <iostream>
#include <queue>
using namespace std;

int N, M;
const int MAXNM = 600;

int arr[MAXNM][MAXNM];
bool v[MAXNM][MAXNM];
int fx[4] = {0,0,-1,1};
int fy[4] = {-1,1,0,0};

bool outofBound(int x, int y) { return (x<0 || x>=N || y<0 || y>=M);}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N >> M;
    queue<pair<int,int>> q;
    char c;
    int answer = 0;


    for(int x=0; x<N; ++x){
        for (int y=0; y<M; ++y){
            cin >> c;
            arr[x][y] = c;
            if (arr[x][y] == 'I'){
                v[x][y] = true;
                q.push({x,y});
            }
        }
    }

    while(!q.empty()){
        pair<int,int> cur = q.front(); q.pop();
        int x = cur.first;
        int y = cur.second;
        for(int f=0; f<4; ++f){
            int nx = x + fx[f];
            int ny = y + fy[f];
            if(!outofBound(nx,ny) && !v[nx][ny] && arr[nx][ny]!= 'X'){
                q.push({nx,ny});
                v[nx][ny] = true;
                if(arr[nx][ny] == 'P') ++answer;
            }
        }
    }

    if (answer == 0) cout << "TT";
    else cout << answer;

    return 0;
}
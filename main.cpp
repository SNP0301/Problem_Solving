/*
    긍정, 책임
    100*100에 대해 완전탐색 100번 = 100만. 가능.

    * 아무 지역도 물에 잠기지 않을 수도 있다.
*/
#include<iostream>
#include<vector>
#include<queue>
#include<set>
using namespace std;
const int MXN = 100;
int arr[MXN][MXN];
bool v[MXN][MXN];
bool done[MXN][MXN];
int N,h;
int fx[4] = {0,0,-1,1};
int fy[4] = {-1,1,0,0};
priority_queue<int,vector<int>,greater<>> height;

bool outofBound(int x, int y){ return(x<0 || x>=N || y<0 || y>=N);}

void resetV(){
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            v[i][j] = false;
        }
    }
}

void bfs(int x, int y){
    queue<pair<int,int>> q;
    q.push({x,y});
    v[x][y] = true;

    while(!q.empty()){
        auto [x,y] = q.front(); q.pop();
        for(int f=0; f<4; ++f){
            int nx = x + fx[f];
            int ny = y + fy[f];
            if(!outofBound(nx,ny) && !v[nx][ny] && !done[nx][ny]){
                v[nx][ny] = true;
                q.push({nx,ny});
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr), cout.tie(nullptr);

    set<int> st;
    int mx = 1; // 모든 지역이 잠기지 않는 경우
    cin >> N;
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            cin >> arr[i][j];
            st.insert(arr[i][j]);
        }
    }

    for(auto e: st){
        height.push(e);
    }

    while(!height.empty()){
        h = height.top(); height.pop();

        // 높이만큼 다 잠기게 만들고
        for(int x=0; x<N; ++x){
            for(int y=0; y<N; ++y){
                if(h >= arr[x][y]) done[x][y] = true;
            }
        }

        // BFS
        int curCnt = 0;
        resetV();
        for(int x=0; x<N; ++x){
            for(int y=0; y<N; ++y){
                if(!v[x][y] && !done[x][y]){
                    bfs(x,y);
                    ++curCnt;
                }
            }
        }

        // 정답 갱신
        if (mx < curCnt) mx = curCnt;

    }

    cout << mx;


    return 0;
}
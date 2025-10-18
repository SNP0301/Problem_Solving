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
#include <algorithm>

using namespace std;
using node = pair<int,int>;

static int N,cnt;
vector<vector<int>> vc;
vector<vector<bool>> v;

int fx[4] = {0,0,-1,1};
int fy[4] = {1,-1,0,0};

bool outofBound(int x, int y){ return (x<0 || x>=N || y<0 || y>=N);}

int BFS(int ix, int iy){
    queue<node> q;
    q.push({ix,iy});
    v[ix][iy] = true;
    int building_cnt = 1;

    while(!q.empty()){
        node cur = q.front(); q.pop();
        int x = cur.first;
        int y = cur.second;
        for(int f=0; f<4; ++f){
            int nx = x+fx[f];
            int ny = y+fy[f];
            if(!outofBound(nx,ny) && vc[nx][ny]==1 && !v[nx][ny]){
                q.push({nx,ny});
                v[nx][ny] = true;
                ++building_cnt;
            }
        }
    }

    return building_cnt;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    string numString;
    vector<int> buildingVc;
    int res;
    cin >> N;
    vc.resize(N);
    v.resize(N);

    for(int i=0; i<N; ++i){
        cin >> numString;
        for(int j=0; j<N; ++j){
            vc[i].push_back(numString[j]-48);
            v[i].push_back(false);
        }
    }

    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            if(vc[i][j]==1 && !v[i][j]){
                res = BFS(i,j);
                buildingVc.push_back(res);
                ++cnt;
            }
        }
    }
    sort(buildingVc.begin(), buildingVc.end());
    cout << cnt << "\n";

    for(const int &building: buildingVc){
        cout << building << "\n";
    }

    return 0;
}
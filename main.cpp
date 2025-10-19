/*
    긍정, 책임
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using sheep = pair<int,int>;

static int H,W;
vector<vector<char>> vc;
vector<vector<bool>> v;

int fx[4] = {0,0,-1,1};
int fy[4] = {-1,1,0,0};

bool outofBound(int ox, int oy){ return (ox<0 || ox>=H || oy<0 || oy>=W); }

void BFS(int bx, int by){
    queue<sheep> q;
    q.push({bx,by});
    v[bx][by] = true;

    while(!q.empty()){
        sheep sh = q.front(); q.pop();
        int x = sh.first;
        int y = sh.second;
        for(int f=0; f<4; ++f){
            int nx = x + fx[f];
            int ny = y + fy[f];
            if(!outofBound(nx,ny) && !v[nx][ny] && vc[nx][ny]=='#'){
                q.push({nx,ny});
                v[nx][ny] = true;
            }
        }
    }

}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int T,answer;
    char c;
    cin >> T;
    for(int t=0; t<T; ++t){
        cin >> H >> W;

        vc.resize(0);
        v.resize(0);

        vc.resize(H);
        v.resize(H);
        answer = 0;

        for(int h=0; h<H; ++h){
            for(int w=0; w<W; ++w){
                cin >> c;
                vc[h].push_back(c);
                v[h].push_back(false);
            }
        }

        for(int x=0; x<H; ++x){
            for(int y=0; y<W; ++y){
                if(vc[x][y]=='#' && !v[x][y]){
                    // cout << x << "," << y << "\n";
                    BFS(x,y);
                    ++answer;
                }
            }
        }

        cout << answer << "\n";
        
    }

    return 0;
}
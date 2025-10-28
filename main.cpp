/*
    긍정, 책임
    
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int I;
const int MAXI = 300;
int arr[MAXI][MAXI];
bool v[MAXI][MAXI];

int edx[] = {-2,-1,1,2,2,1,-1,-2};
int edy[] = {1,2,2,1,-1,-2,-2,-1};

bool outofBound(int x, int y){ return(x<0 || x>=I || y<0 || y>=I);}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int T,sx,sy,ex,ey;
    cin >> T;
    for(int t=0; t<T; ++t){
        cin >> I >> sx >> sy >> ex >> ey;


        // 00. 초기화
        for(int x=0; x<I; ++x){
            for(int y=0; y<I; ++y){
                arr[x][y] = 0;
                v[x][y] = false;
            }
        }

        // 01. 
        queue<pair<int,int>> q;
        q.push({sx,sy});
        v[sx][sy] = true;

        while(!q.empty()){
            auto [x,y] = q.front(); q.pop();
            if (x == ex && y == ey){
                cout << 0 << "\n";
                break;
            }
            for(int e=0; e<8; ++e){
                int nx = x + edx[e];
                int ny = y + edy[e];
                if(!outofBound(nx,ny) && !v[nx][ny]){
                    q.push({nx,ny});
                    v[nx][ny] = true;
                    arr[nx][ny] = arr[x][y] + 1;
                    if(nx == ex && ny == ey){
                        q = {};
                        cout << arr[nx][ny] << "\n";
                        break;
                    }
                }
            }
        }

    }

    return 0;
}
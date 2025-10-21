/*
    긍정, 책임

    0이 하양, 1이 파랑 출력은 하얀 다음 파랑
    128*128에 대해 완전탐색 7번
*/
#include <iostream>
using namespace std;

const int MAXN = 128;
static int N;
int arr[MAXN][MAXN];
bool v[MAXN][MAXN];



int pow(int n, int to){
    int multiple = n;
    for(int i=1; i<to; ++i){
        n *= multiple;
    }
    return n;
}

bool outofBound(int x, int y){ return(x<0 || x>=N || y<0 || y>=N);}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int num;
    int white = 0; // 0이 하양
    int blue = 0; // 1이 파랑
    cin >> N;

    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            cin >> num;
            arr[i][j] = num;
        }
    }

    for(int sz=N; sz>0; sz/=2){ // 8 4 2 1
        for(int x=0; x<N; ++x){
            for(int y=0; y<N; ++y){
                if(!v[x][y]){ // 아직 세지 않은 곳이면
                    int cur = arr[x][y]; // 지금 색
                    bool possible = true;
                    for(int lx=0; lx<sz; ++lx){
                        for(int ly=0; ly<sz; ++ly){
                            if(arr[x+lx][y+ly]!=cur || v[x+lx][y+ly] || outofBound(x+lx,y+ly)){
                                possible = false;
                                break;
                            }
                        }
                        if(!possible) break;
                    }
                    if (possible){
                        int cnt = 0;
                    for(int lx=0; lx<sz; ++lx){
                        for(int ly=0; ly<sz; ++ly){
                            ++cnt;
                            v[x+lx][y+ly] = true;
                        }
                    }
                    if (arr[x][y] == 0) white += cnt;
                    else blue += cnt;
                }
            }
        }
    }


    cout << white << "\n" << blue;

    return 0;
}
}
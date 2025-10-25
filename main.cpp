/*
    긍정, 책임
    
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAXNM = 50;
static int answer = 0;
bool v[MAXNM][MAXNM];
char arr[MAXNM][MAXNM];

int N,M;

bool outofBound(int x, int y) {return (x<0 || x>=N || y<0 || y>=M);}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N >> M;

    for(int x=0; x<N; ++x){
        for(int y=0; y<M; ++y){
            cin >> arr[x][y];
        }
    }

    for(int x=0; x<N; ++x){
        for(int y=0; y<M; ++y){
            if(!v[x][y]){
                ++answer;
                if(arr[x][y] == '-'){
                    int sz = 1;
                    while(!outofBound(x,y+sz) && arr[x][y+sz]=='-'){
                        v[x][y+sz] = true;
                        ++sz;
                    }
                }
                else{
                    int sz = 1;
                    while(!outofBound(x+sz,y) && arr[x+sz][y]=='|'){
                        v[x+sz][y] = true;
                        ++sz;
                    }
                }
            }
        }
    }



    cout << answer;


    return 0;
}
/*
    긍정, 책임
*/
#include <iostream>
using namespace std;
static char arr[51][51];

int main(){
    int answer = 8*8+1;
    int N, M;
    cin >> N >> M;

    for (int x=0; x<N; ++x){
        for (int y=0; y<M; ++y){
            cin >> arr[x][y];
        }
    }


    for (int x=0; x<N-8+1; ++x){
        for (int y=0; y<M-8+1;++y){
            // W로 시작하는 board에 맞추는 경우
            int wAnswer = 0;
            for (int ix=0; ix<8; ++ix){
                for (int iy=0; iy<8; ++iy){
                    if ((x+ix+y+iy)%2 == 0 && arr[x+ix][y+iy]=='B') ++wAnswer;
                    if ((x+ix+y+iy)%2 == 1 && arr[x+ix][y+iy]=='W') ++wAnswer;
                }
            }

            // B로 시작하는 board에 맞추는 경우
            int bAnswer = 0;
            for (int ix=0; ix<8; ++ix){
                for (int iy=0; iy<8; ++iy){
                    if ((x+ix+y+iy)%2 == 0 && arr[x+ix][y+iy]=='W') ++bAnswer;
                    if ((x+ix+y+iy)%2 == 1 && arr[x+ix][y+iy]=='B') ++bAnswer;
                }
            }
            int curAnswer = min(wAnswer, bAnswer);
            answer = min(answer,curAnswer);
        }
    }
    cout << answer;

    return 0;
}
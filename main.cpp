/*
    긍정

    사람 안 변한다
*/

#include <iostream>
#include <vector>


using namespace std;

// int myPrint(vector<vector<char>> vc){
//     int N = size(vc); // sizeof는 멤버변수 크기만 돌려줌 ㅇㅇㅇ 객체 자체 크기를 구하는게 아니니까 size 쓸 것
//     int M = size(vc[0]);
//     cout << "N: " << N;
//     cout << "M: " << M;

//     for (int i = 0; i<N; i++){
//         for (int j = 0; j<M; j++){
//             cout << vc[i][j];
//         }
//         cout << "\n";
//     }
//     return 0;
// }

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<vector<char>> vc(N);
    for (int i = 0; i<N; i++){
        for (int j = 0;j<M;j++){
            char c;
            cin >> c;
            vc[i].push_back(c);
        }
    }

    int answer = 8*8+1;

    for (int i =0; i<=N-8;i++){
        for (int j =0; j<=M-8;j++){
            int w_answer = 0;
            int b_answer = 0;   
            for (int ni=0; ni<8; ni++){
                for (int nj=0; nj<8; nj++){
                    if((ni+nj)%2==0 && vc[i+ni][j+nj] == 'B') w_answer ++;
                    else if((ni+nj)%2==1 && vc[i+ni][j+nj] == 'W') w_answer ++;
                    else if((ni+nj)%2==1 && vc[i+ni][j+nj] == 'B') b_answer ++;
                    else if((ni+nj)%2==0 && vc[i+ni][j+nj] == 'W') b_answer ++;
                }
            }
            int cur_answer = min(w_answer,b_answer);
            answer = min(answer,cur_answer);
        }
    }




    cout << answer;
    return 0;
}
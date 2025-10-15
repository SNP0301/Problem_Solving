/*
    긍정, 책임
*/

#include <iostream>
using namespace std;

const int MAXN = 2'000'001;

int main(){
    int N;
    cin >> N;

    int arr[MAXN];
    int startIdx = 1;
    int endIdx = N;

    for (int i=1; i<N+1; ++i){
        arr[i] = i;
    }

    while (true){
        if (startIdx == endIdx){
            cout << arr[startIdx];
            break;
        }

        // 맨 위 카드 버리기
        ++startIdx;

        // 맨 위 카드를 맨 밑으로 넣기
        arr[endIdx+1] = arr[startIdx];
        ++endIdx;
        ++startIdx;

    }

    return 0;
}
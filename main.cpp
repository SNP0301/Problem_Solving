/*
    긍정, 책임

    array로 도전
*/
#include <iostream>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
    int arr[10'000] = {-1,};
    int N,num;
    int startIdx = 0;
    int endIdx = -1;
    cin >> N;

    string cmd;

    for(int i=0; i<N; ++i){
        cin >> cmd;
        if (cmd == "push"){
            cin >> num;
            arr[++endIdx] = num;
        }
        else if(cmd == "pop"){
            if (endIdx < startIdx) cout << -1 << "\n";
            else cout << arr[startIdx++] << "\n";
        }
        else if(cmd == "size") cout << endIdx-startIdx+1 << "\n";
        else if(cmd == "empty"){
            if (endIdx < startIdx) cout << 1 << "\n";
            else cout << 0 << "\n";
        }
        else if(cmd == "front"){
            if(endIdx < startIdx) cout << -1 << "\n";
            else cout << arr[startIdx] << "\n";
        }
        else if(cmd == "back"){
            if(endIdx < startIdx) cout << -1 << "\n";
            else cout << arr[endIdx] << "\n";
        }

    }

    return 0;
}
/*
    긍정, 책임
    추억이 새록새록
*/
#include <iostream>
#include <queue>
using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int X,cmd;
    cin >> X;
    priority_queue<int> pq;

    for(int x=0; x<X; ++x){
        cin >> cmd;
        cmd = cmd*-1;
        if (cmd == 0){
            if (pq.empty()) cout << 0 << "\n";
            else{
                int res = pq.top(); pq.pop();
                cout << res*-1 << "\n";
            }
        }
        else pq.push(cmd);
    }

    return 0;
}
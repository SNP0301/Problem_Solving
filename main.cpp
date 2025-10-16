/*
    긍정, 책임

    X가 3으로 나누어 떨어지면, 3으로 나눈다.
    X가 2로 나누어 떨어지면, 2로 나눈다.
    1을 뺀다.

*/
#include <iostream>
#include <queue>
using namespace std;

const static int MAXN = 1'000'000+1;
int arr[MAXN] = {MAXN};
bool v[MAXN] = {false};

int main(){
    int N;
    cin >> N;

    queue<int> q;
    q.push(N);

    arr[N] = 0;
    v[N] = true;

    while (!q.empty()){
        int cur = q.front(); q.pop();

        int curScore = arr[cur];
        
        if (cur == 1){ // 종료 조건
            cout << arr[cur];
            return 0;
        }

        if(cur%3 == 0 && !v[cur/3]){
            q.push(cur/3);
            v[cur/3] = true;
            arr[cur/3] = curScore + 1;
        }
        if (cur%2 == 0 && !v[cur/2]){
            q.push(cur/2);
            v[cur/2] = true;
            arr[cur/2] = curScore + 1;
        }
        if (cur-1 >= 0 && !v[cur-1]){
            q.push(cur-1);
            v[cur-1] = true;
            arr[cur-1] = curScore +1;
        }
        
    }

    return 0;
}
/*
    긍정, 책임
*/
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <queue>
using namespace std;

// const static int MAX = 1'000'000'000;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    long A,B;
    cin >> A >> B;

    unordered_map<long,long> mp;
    unordered_set<long> v;
    queue<long> q;

    mp[A] = 0;
    q.push(A);
    v.insert(A);

    while(!q.empty()){
        long cur = q.front(); q.pop();
        if (cur == B) break;
        long nxtArr[2] = {cur*2, cur*10+1};

        for(long nxt: nxtArr){
            if(v.find(nxt) == v.end() && nxt <= B){ // 못 찾았으면 = 간 적 없으면
                q.push(nxt);
                v.insert(nxt);
                mp[nxt] = mp[cur]+1;
            }
        }
    }
    
    if(v.find(B) == v.end()) cout << -1;
    else cout << mp[B]+1;

    return 0;
}
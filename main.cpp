/*
    긍정, 책임
    
*/
#include <iostream>
#include <queue>
#include <vector>
#include <set>
using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N,M,num;
    set<int> st;
    cin >> N;
    for(int i=0; i<N; ++i){
        cin >> num;
        st.insert(num);
    }

    cin >> M;
    for(int i=0; i<M; ++i){
        cin >> num;
        if(st.find(num) == st.end()) cout << 0 << " ";
        else cout << 1 << " ";
    }

    return 0;
}
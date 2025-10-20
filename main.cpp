/*
    긍정, 책임

    Map에 넣어두고, Key값을 NlgN으로 정렬 N 최대값은 1'000'000
        -> 1'000'000 * lg 1'000'000 = 6'000'000
*/
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N,num;
    set<int> st;
    vector<int> vc;
    unordered_map<int, int> map;

    cin >> N;
    int idx = 0;
    for(int i=0; i<N; ++i){
        cin >> num;
        st.insert(num);
        vc.push_back(num);
    }

    for(const int &e : st){
        map[e] = idx++;
    }

    for(int i=0; i<N; ++i){
        cout << map[vc[i]] << " ";
    }



    return 0;
}
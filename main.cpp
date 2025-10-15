/*
    긍정, 책임
    유클리드 호제법
*/
#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct pair<int,int> point;

int main(){
    int N,x,y;
    cin >> N;
    vector<point> vc;
    for(int i=0; i<N; ++i){
        cin >> x >> y;
        vc.push_back(point(x,y));
    }
    sort(vc.begin(),vc.end());
    
    for (int i=0; i<N; ++i) {
        cout << vc[i].first << " " << vc[i].second << '\n';
    }   
    return 0;
}
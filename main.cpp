// 긍정


#include <iostream>
#include <unordered_set>

using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int N, M;
    cin >> N;
    
    unordered_set<int> s;
    for(int i=0; i<N; i++){
        int n;
        cin >> n;
        s.insert(n);
    }

    cin >> M;
    for(int i=0; i<M; i++){
        int m;
        cin >> m;
        cout << s.count(m) << " ";
    }

    return 0;
}
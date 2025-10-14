/*
    긍정, 책임
*/

#include <iostream>
#include <unordered_set>



using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N,num;
    cin >> N;
    unordered_set<int> st = {};

    for (int i=0; i<N; ++i){
        cin >> num;
        st.insert(num);
    }

    cin >> N;
    for(int i=0; i<N; ++i){
        cin >> num;
        if(st.find(num) != st.end()) cout << 1;
        else cout << 0;
        cout << "\n";
    }


    return 0;
}
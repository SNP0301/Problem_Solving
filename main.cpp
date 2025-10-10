/*
    긍정, 책임

    컴파일 에러 1회: #include <vector>를 포함하지 않았다.
*/
#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; 
    if(!(cin >> N)) return 0;

    vector<int> st;
    st.reserve(N);
    int top = 0;

    for(int i=0;i<N;i++){
        int cmd; cin >> cmd;

        if(cmd == 1){
            int X; cin >> X;
            if(top < (int)st.size()) st[top] = X;
            else st.push_back(X);
            ++top;
        }
        else if(cmd == 2){
            if(top == 0) cout << -1 << '\n';
            else cout << st[--top] << '\n';
        }
        else if(cmd == 3){
            cout << top << '\n';
        }
        else if(cmd == 4){
            cout << (top == 0) << '\n';
        }
        else if(cmd == 5){
            if(top == 0) cout << -1 << '\n';
            else cout << st[top-1] << '\n';
        }
    }
    return 0;
}

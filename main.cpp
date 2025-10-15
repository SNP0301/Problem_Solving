/*
    긍정, 책임
*/
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
    int N,num;
    cin >> N;
    vector<int> vc;
    for(int i=0; i<N; ++i){
        string cmd;
        cin >> cmd;
        if (cmd == "push"){
            cin >> num;
            vc.push_back(num);
        }
        else if (cmd == "pop"){
            if (vc.empty()) cout << -1 << "\n";
            else{
                cout << vc.back() << "\n";
                vc.pop_back();
            }
        }
        else if (cmd == "size") cout << vc.size() << "\n";
        else if (cmd == "empty"){
            if (vc.empty()) cout << 1 << "\n";
            else cout << 0 << "\n";
        }
        else if (cmd == "top"){
            if (vc.empty()) cout << -1 << "\n";
            else cout << vc.back() << "\n";
        }

    }

    return 0;
}
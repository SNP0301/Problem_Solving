/*
    긍정, 책임
*/
#include <iostream>
#include <string>

using namespace std;

int main(){
    int T;
    cin >> T;

    for(int i=0; i<T; ++i){
        string s;
        cin >> s;
        int l = 0;
        int r = 0;
        bool isVPS = true;
        for(int j=0; j<(int)s.length(); ++j){
            if (s[j] == '(') ++l;
            else if (s[j] == ')'){
                ++r;
                if (l > 0){
                    --l;
                    --r;
                }
                else if (l <= 0){
                    isVPS = false;
                    break;
                }
            }
        }
        if (l>0 || r>0) isVPS = false;
        if (isVPS) cout << "YES\n";
        else cout << "NO\n";
    }



    return 0;
}
/*
    긍정, 책임
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

char arr[10'000][10+1];

struct Trie{
    bool endofWord;
    Trie* children[10]; // 0부터 9까지 10자리

    Trie(): endofWord(false), children{}{
    }

    void insert(char* key){
        if(*key == '\0') endofWord = true;
        else{
            int idx = *key - '0';
            if(children[idx] == 0) children[idx] = new Trie();
            children[idx]->insert(key+1);
        }
    }


    bool find(char* key){
        if(*key == '\0') return true;
        if(endofWord) return false;
        int idx = *key - '0';
        return children[idx]->find(key+1);
    }
};

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int T, N;
    cin >> T;

    for(int i=0; i<T; ++i){
        Trie* root = new Trie();
        cin >> N;

        for(int j=0; j<N; ++j){
            cin >> arr[j];
            root -> insert(arr[j]);
        }

        bool isPossible = true;
        for(int j=0; j<N; ++j){
            if(root -> find(arr[j]) == false){
                isPossible = false;
                break;
            }
        }

        if(isPossible) cout << "YES\n";
        else cout << "NO\n";
        delete root; // 에반데
    }


    return 0;
}
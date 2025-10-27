/*
    긍정, 책임
*/
#include <iostream>
#include <string>
using namespace std;
string s;

struct Trie{
    bool endofWord;
    int sameCnt;
    Trie* children[26]; // 알파벳 소문자 26개

    Trie(): endofWord(false), sameCnt(0), children{}{
    }

    void insert(string& s, int idx, bool possible){

        if(idx >= (int)s.length()){
            sameCnt++;
            if(sameCnt > 1) cout << sameCnt;
            cout << "\n";
            return;
        }

        int ctoi = s[idx] - 'a';
        if(!possible) cout << s[idx];

        if(!children[ctoi]){
            children[ctoi] = new Trie();
            possible = true; // 없네
        }

        children[ctoi]->insert(s,idx+1,possible);
    
    }
};

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N;
    cin >> N;
    Trie* root = new Trie();

    for(int i=0; i<N; ++i){
        cin >> s;
        root -> insert(s,0,false); // 모르니까
    }

    delete root;
    return 0;
}
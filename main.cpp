/*
    긍정, 책임
*/
#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N, M;
    string id;
    unordered_set<string> dst, bst;
    vector<string> answer;

    cin >> N >> M;

    for(int i=0; i<N; ++i){
        cin >> id;
        dst.insert(id);
    }

    for(int i=0; i<M; ++i){
        cin >> id;
        bst.insert(id);
    }

    if (N>M){
        for(string id: bst){
            if(dst.count(id)){
                answer.push_back(id);
            }
        }
    }
    else {
        for(string id: dst){
            if(bst.count(id)){
                answer.push_back(id);
            }
        }
    }

    sort(answer.begin(), answer.end());

    cout << (int)answer.size() << "\n";
    for (string id: answer){
        cout << id << "\n";
    }



    return 0;
}
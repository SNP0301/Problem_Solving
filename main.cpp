/*
    긍정, 책임
    23:08 ~ 
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N, num;
    int answer = 0;
    cin >> N;
    vector<int> vc;
    vector<int> fromLeft;
    vector<int> fromRight;

    for(int i=0; i<N; ++i){
        cin >> num;
        vc.push_back(num);
        fromLeft.push_back(1);
        fromRight.push_back(1);
    }

    for(int i=0; i<N; ++i){
        for(int j=0; j<i; ++j){
            if(vc[i]>vc[j] && fromLeft[i] < fromLeft[j]+1) fromLeft[i] = fromLeft[j]+1;
        }
    }

    for(int i=N-1; i>=0; --i){
        for(int j=i+1; j<N; ++j){
            //cout << i << " " << j << "\n";
            if(vc[i]>vc[j] && fromRight[i] < fromRight[j]+1) fromRight[i] = fromRight[j]+1;
        }
    }


    for(int i=0; i<N; ++i){
        answer = max(answer,fromRight[i]+fromLeft[i]-1);
        //cout << fromRight[i] + fromLeft[i] << "\n";
    }

    cout << answer;


    return 0;
}
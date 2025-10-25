/*
    긍정, 책임
    22:35 ~ 
    순서대로 정렬했을 때, 내가 봤을 때, 나보다 바로 한 계층 작은 애 + 나?
*/
#include <iostream>
#include <queue>
#include <vector>
#include <set>
using namespace std;

const int MAXN = 1'000 + 1; // 1based
int dp[MAXN];


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N,num;
    int answer = -1;
    cin >> N;
    vector<int> vc;
    vector<int> dp;

    for(int i=0; i<N; ++i){
        cin >> num;
        vc.push_back(num);
        dp.push_back(1);
    }

    for(int i=0; i<N; ++i){
        for(int j=0; j<i; ++j){
            if(vc[i] < vc[j] && dp[i] < dp[j] + 1) dp[i] = dp[j] + 1;
        }
        answer = max(answer, dp[i]);
    }

    // for(auto num: dp){
    //     cout << num << "\n";
    // }
    cout << answer;
    return 0;
}
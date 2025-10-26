/*
    긍정, 책임
    LIS O(LlgN)의 핵심.
    LIS 길이가 결과적으로 L이라 할 때, L개 요소에 대해 각각 이분탐색 1번씩 실행하므로 L * lgN = LlgN
        - LIS를 만드는게 아니라, LIS 누적표를 만든다 생각하자
        - **길이 n짜리 증가 수열의 끝값
    lower_bound가 end를 반환했으면 추가, 그렇지 않으면 갱신

    * 함수에 vector를 인자로 건네주기
        - const vector<int>& A의 경우
            1) &: 복사하지 않고 참조(주소로 접근)하겠다

*/
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int getLisLength(const vector<int>& A){
    vector<int> Lis;

    for(auto x: A){
        auto it = lower_bound(Lis.begin(),Lis.end(), x);
        if(it == Lis.end()) Lis.push_back(x);
        else *it = x;
    }

    return (int)Lis.size();
}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N, num;
    vector<int> vc;

    cin >> N;
    for(int i=0; i<N; ++i){
        cin >> num;
        vc.push_back(num);
    }

    cout << getLisLength(vc);

    return 0;
}
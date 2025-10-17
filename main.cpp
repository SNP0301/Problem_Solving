/*
    긍정, 책임
    1 |
    2 ||, =
    3 |||, |=, =| 
    5 ||||, ==, ||=, =||, |=|
    
*/
#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int answer[1001] = {0,};
    answer[1] = 1;
    answer[2] = 2;
    int N;
    cin >> N;

    for(int i=3; i<=N; ++i){
        answer[i] = ((answer[i-1]%10007) + (answer[i-2]%10007))%10007;
    }

    cout << answer[N]%10007;
    return 0;
}
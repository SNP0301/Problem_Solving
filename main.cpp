#include <iostream>
using namespace std;

static long long int A,B,C;

long long solve(long num){
    long long halfNum = num / 2;
    if (num == 0) return 1;
    else if (num == 1) return A%C;
    else {
        long long curNum = solve(halfNum)%C;
        if (num%2 == 1) return (curNum * curNum % C) *(A%C);
        else return curNum * curNum % C;
    }
}

int main(){
    cin >> A >> B >> C;
    cout << solve(B)%C;

    return 0;
}
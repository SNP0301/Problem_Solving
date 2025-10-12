#include <iostream>

int binarySerach(int n){
    int s,e,m;
    s = 1;
    e = n/2;
    m = 0;

    while (s <= e){
        m = (s+e)/2;
        int target = m*m;

        if(target > n || target <= 0) e = m - 1;
        else if (target < n) s = m + 1;
        else break;
    }

    if(n > m * m) ++m;
    return m;
}

bool isPrime(int n){
    if (n == 1) return false;
    if (n == 2) return true;
    for (int i=2; i<binarySerach(n)+1; ++i){
        if (n%i == 0) return false;
    }
    return true;
}

int main(){

    int N, answer,num;
    std::cin >> N;
    answer = 0;
    for (int j=0; j<N; ++j){
        std::cin >> num;
        if (isPrime(num)) answer += 1;
    }

    std::cout << answer;
    return 0;
}
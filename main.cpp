#include <iostream>

static int t;

int getBundle(int pNum){ // 신청한 people 수, 묶음 크기
    if (pNum == 0) return 0;
    else if (pNum%t== 0) return pNum/t;
    else return (pNum/t)+1;
}

int main(){

    int n,s, m, l, xl, xxl, xxxl, p, tAnswer;
    std::cin >> n >> s >> m >> l >> xl >> xxl >> xxxl >> t >> p;
    tAnswer = getBundle(s) + getBundle(m) + getBundle(l) + getBundle(xl) + getBundle(xxl) + getBundle(xxxl);
    std::cout << tAnswer << "\n";
    std::cout << n/p << " " << n%p;
    return 0;
}
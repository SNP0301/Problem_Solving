#include <iostream>

int main(){
    int A,B,C;

    while (true){
        std::cin >> A >> B >> C;
        if (A==0 && B==0 && C==0) break;
        if (A*A == B*B + C*C || B*B == C*C + A*A || C*C == B*B + A*A) std::cout << "right\n";
        else std::cout << "wrong\n";
    }

    return 0;
}
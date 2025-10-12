#include <iostream>


int main(){
    int A,B,T;
    std::cin >> T;
    for (int i=0; i<T; ++i){
        std::cin >> A >> B;
        std::cout << A+B << "\n";
    }


    return 0;
}
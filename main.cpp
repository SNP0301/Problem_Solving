#include <iostream>

int main(){

    int T,R;
    std::string S;
    std::cin >> T;

    for (int i=0; i<T; ++i){
        std::cin >> R >> S;
        for (int j=0; j<(int)S.size();++j){
            for (int k=0; k<R; ++k){
                std::cout << S[j];
            }
        }
        std::cout << "\n";
    }

    return 0;
}
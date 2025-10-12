#include <iostream>
#include <vector>

int main(){

    int N, M, curNum;
    int mx = -1;
    std::vector <int> vc;
    std::cin >> N >> M;
    for(int i=0; i<N; ++i){
        std::cin >> curNum;
        vc.push_back(curNum);
    }

    for(int i=0; i<N-2; ++i){
        for(int j=i+1; j<N-1; ++j){
            for(int k=j+1; k<N; ++k){
                if (vc[i]+vc[j]+vc[k] > mx && vc[i]+vc[j]+vc[k] <= M) mx = vc[i]+vc[j]+vc[k];
            }
        }
    }

    std::cout << mx;
    return 0;
}
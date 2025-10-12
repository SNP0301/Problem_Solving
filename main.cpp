#include <iostream>

int main(){

    int N,num;
    std::cin >> N;

    int mnNum = 1'000'000+1;
    int mxNum = -1'000'000-1;

    for(int i=0;i<N;++i){
        std::cin >> num;
        if (num > mxNum) mxNum = num;
        if (num < mnNum) mnNum = num;
    }

    std::cout << mnNum << " " << mxNum;
    

    return 0;
}
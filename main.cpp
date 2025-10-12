#include <iostream>

int main(){
    
    int num;
    int answerNum = -1;
    int answerIdx = -1;

    for(int i=1;i<10;++i){
        std::cin >> num;
        if (num > answerNum){
            answerNum = num;
            answerIdx = i;
        }
    }
    
    std::cout << answerNum << "\n";
    std::cout << answerIdx;

    return 0;
}
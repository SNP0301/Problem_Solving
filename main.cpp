#include <iostream>
#include <vector>

int main(){
    int N,answer;
    answer = 0;
    std::cin >> N;

    std::string number;
    std::cin >> number;
    for (int i =0; i<N; i++){
        answer += (int)number[i]-48;
    }
    std::cout << answer;

    return 0;
}
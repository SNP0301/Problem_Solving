#include <iostream>

int main(){
    std::string num;
    while (true){
        std::cin >> num;
        bool isPalindrome = true;
        if (num == "0") break;
        for (int i=0; i<(int)num.size(); ++i){
            if (num[i] != num[(int)num.size()-i-1]) isPalindrome = false;
        }
        std::string answer = (isPalindrome) ? "yes" : "no";
        std::cout << answer << "\n";
    }
    

    return 0;
}
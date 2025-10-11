#include <iostream>
#include <vector>

using namespace std;

static long first = 0;

long fib(int n){
    if (n == 1 || n == 2){
        ++first;
        return 1;
    }
    else return (fib(n-1)+fib(n-2));
}

int main(){
    int n;
    cin >> n;
    fib(n);
    cout << first << " " << n-2;


    return 0;
}
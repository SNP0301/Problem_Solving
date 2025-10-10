/*
    긍정, 책임

    ---
    1
    1
    100
    ---
    1
    1
    -100
    ---
    11
    1 4 1 2 4 2 4 2 3 4 4
    -100
    ---
*/

#include <iostream>

using namespace std;

int main (){
    int n,v,tmp;
    cin >> n;
    int arr[201+1]={0,};

    for (int i = 0; i<n; i++){
        cin >> tmp;
        arr[tmp+100]++;
    }

    cin >> v;
    cout << arr[v+100];
    return 0;
}
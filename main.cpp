#include <iostream>
#include <vector>

using namespace std;

int main(){
    float N,num;
    float mx = -1;
    float newSum = 0;
    vector <int> vc;

    cin >> N;

    for (int i=0; i<N; ++i){
        cin >> num;
        vc.push_back(num);
        if (num >= mx) mx = num;
    }

    for (int i=0; i<N; ++i){
        newSum += (vc[i]/mx)*100;

    }
    cout.precision(10);
    cout << float(newSum/N);


    return 0;
}
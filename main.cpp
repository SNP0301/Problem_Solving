/*
    긍정, 책임

    5
    3 1 4 3 2
    로 들어오면

    정렬해보면 1 2 3 3 4
    누적합하면 1 3 6 9 13
    누적합을 총합하면 1+3+6+9+13 = 32

    1) 정렬 O(N log N)
    2) 누적합   O(N)
    3) 누적합을 총합 O(N)
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;



void merge(){

}

void mergeSort(){

}



int main(){
    int N,p;
    int answer = 0;
    vector<int> waitTime,accTime;


    cin >> N;
    for(int i=0; i<N; ++i){
        cin >> p;
        waitTime.push_back(p);
        accTime.push_back(0);
    }

    sort(waitTime.begin(),waitTime.end());

    accTime[0] = waitTime[0];
    for(int i=1; i<N; ++i){
        accTime[i] = waitTime[i]+accTime[i-1];
    }

    for(int i=0; i<N; ++i){
        answer += accTime[i];
    }

    cout << answer;


    return 0;
}

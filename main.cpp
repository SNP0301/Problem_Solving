/*
    lexicographically 라는 말이 잇네
*/

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

typedef struct member {
    int age;
    string name;
    int signInTime;
}member;

bool compareMembers(const member &aMember, const member &bMember){
    if(aMember.age == bMember.age) return aMember.signInTime < bMember.signInTime;
    return aMember.age < bMember.age;
}

int main(){
    int T, age;
    string s;
    cin >> T;
    vector<member> memberVc;

    for(int t=0; t<T; ++t){
        cin >> age >> s;
        memberVc.push_back({age,s,t});
    }

    sort(memberVc.begin(), memberVc.end(), compareMembers);

    for (const auto &m : memberVc) {
        cout << m.age << " " << m.name << "\n";
    }


    return 0;
}
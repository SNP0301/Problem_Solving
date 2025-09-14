#include <iostream>
#include <vector>
#include <array>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s; 
    cin >> s;
    int n = (int)s.size();

    int q; 
    cin >> q;

    // pref[i][c] = s[0..i-1]에서 문자('a'+c)의 개수
    vector<array<int,26>> pref(n+1);
    pref[0].fill(0);

    for (int i = 1; i <= n; ++i) {
        pref[i] = pref[i-1];               // 직전 누적값 복사(26개 한 번에)
        ++pref[i][s[i-1] - 'a'];           // 현재 문자만 +1
    }

    while (q--) {
        char a; int l, r;
        cin >> a >> l >> r;                // 예: a 0 5
        int idx = a - 'a';
        cout << (pref[r+1][idx] - pref[l][idx]) << '\n';
    }
    return 0;
}


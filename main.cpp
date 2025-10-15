#include <iostream>
using namespace std;

const int MAXN = 1001;
int P[MAXN];        // 순열
bool visited[MAXN]; // 방문 여부
int N;

void dfs(int cur) {
    visited[cur] = true;
    int next = P[cur];
    
    if (!visited[next]) {
        dfs(next);
    }
}

int main() {
    int T;
    cin >> T;
    for (int j=0; j<T; ++j){
        for(int i=0; i<MAXN; ++i){
            P[i] = 0;
            visited[i] = false;
        }
        cin >> N;
        for (int i = 1; i <= N; ++i) {
            cin >> P[i];
        }

        int cycleCount = 0;

        for (int i = 1; i <= N; ++i) {
            if (!visited[i]) {
                dfs(i);
                ++cycleCount;
            }
        }

        cout << cycleCount << '\n';
    }

    return 0;
}

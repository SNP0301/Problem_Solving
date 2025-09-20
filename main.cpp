#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int INF = 21*21 + 1;

int N;
vector<vector<int>> arr; // main에서 선언하면 bfs에서 못 먹는다
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

// 먹을래 말래
bool bfs(int sx, int sy, int sz, int &d, int &ox, int &oy) {
    vector<vector<int>> dist(N, vector<int>(N, -1));
    queue<pair<int,int>> q;
    q.push({sx, sy});
    dist[sx][sy] = 0;

    int bestDist = INF;
    int bx = INF;
    int by = INF;

    while (!q.empty()) {
        auto [x, y] = q.front(); 
        q.pop(); 
        int d = dist[x][y];

        if (d > bestDist) continue;

        for (int f = 0; f < 4; ++f) { // f of four
            int nx = x + dx[f];
            int ny = y + dy[f];

            if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
            if (dist[nx][ny] != -1) continue;
            if (arr[nx][ny] > sz) continue;

            dist[nx][ny] = d + 1;

            if (arr[nx][ny] != 0 && arr[nx][ny] < sz) {
                int nd = d + 1;
                if (nd < bestDist ||
                   (nd == bestDist && (nx < bx || (nx == bx && ny < by)))) { // 하
                    bestDist = nd;
                    bx = nx;
                    by = ny;
                }
            }
            q.push({nx, ny});
        }
    }

    if (bestDist == INF) return false; // 해당사항 없으면

    d = bestDist;
    ox = bx;
    oy = by;
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    arr.assign(N, vector<int>(N));
    int sx = -1, sy = -1;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> arr[i][j];
            if (arr[i][j] == 9){
                sx = i;
                sy = j;
            }
        }
    }
    if (sx != -1) arr[sx][sy] = 0;

    int sz = 2;
    int eaten = 0;
    int answer = 0;
    int x = sx;
    int y = sy;

    while (true) {
        int d, tx, ty;
        if (!bfs(x, y, sz, d, tx, ty)) break; // 못 먹으면 break

        answer += d;
        arr[tx][ty] = 0;
        x = tx;
        y = ty;

        if (++eaten == sz){
            eaten = 0;
            ++sz;
        }
    }

    cout << answer << '\n';
    return 0;
}

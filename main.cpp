/*
    긍정    

    차력쇼 구경할 때가 좋았어,,,,,,,,,,,
*/

#include <iostream>
#include <vector>

using namespace std;

int dy[] = {0, 1, 0, -1};
int dx[] = {1, 0, -1, 0};
int N, K;

vector<vector<int>> board;

int get_mn() {
    int mn = 2147483647;
    for (int i = 0; i < N; ++i){
        if (board[0][i] != -1 && board[0][i] < mn) mn = board[0][i];
    }
    return mn;
}
int get_mx() {
    int mx = -2147483648;
    for (int i = 0; i < N; ++i){
        if (board[0][i] != -1 && board[0][i] > mx) mx = board[0][i];
    }
    return mx;
}

bool if_end() {
    int mx_fishes = get_mx();
    int mn_fishes = get_mn();
    return ((mx_fishes - mn_fishes) <= K);
}

void move_fish() {
    vector<vector<int>> new_board = board; // 가능

    for (int x = 0; x < N; ++x) {
        for (int y = 0; y < N; ++y) {
            if (board[y][x] == -1) continue;
            for (int f = 0; f < 4; ++f) { // f of four
                int nx = x + dx[f];
                int ny = y + dy[f];
                if (ny < 0 || nx < 0 || ny >= N || nx >= N || board[ny][nx] == -1) continue;
                new_board[y][x] += (int)((board[ny][nx] - board[y][x]) / 5);
            }
        }
    }

    vector<int> flat_bowl;

    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            if (new_board[x][y] == -1) continue;
            flat_bowl.push_back(new_board[x][y]);
        }
    }

    board = vector<vector<int>>(N, vector<int>(N, -1));
    board[0] = flat_bowl;
}

void roll() {
    int rx = 1, ry = 1; // 말아올리는 직사각형 가로세로길이 
    int sx = 0;

    int min_fishes = get_mn();
    for (int i = 0; i < N; ++i) if (board[0][i] == min_fishes) board[0][i]++; // 일단 하나씩 주고 시작

    // 말아올리기
    while (sx + rx + ry <= N) {
        for (int x = 0; x < rx; ++x) {
            for (int y = 0; y < ry; ++y) {
                int nx = ry - y;
                int ny = sx + ry + x;
                board[nx][ny] = board[x][y + sx];
                board[x][y + sx] = -1; // 비우기
            }
        }
        sx += ry;
        if (rx == ry) rx++;
        else ry++;
    }

    move_fish();


    // 절반씩 쌓아올리기
    sx = 0;
    rx = 1;
    ry = N / 2;
    for (int i = 0; i < 2; ++i) {
        for (int x = 0; x < rx; ++x) {
            for (int y = 0; y < ry; ++y) {
                int nx = 2 * rx - x - 1;
                int ny = 2 * ry + sx - y - 1; // YEAH
                board[nx][ny] = board[x][y + sx];
                board[x][y + sx] = -1;
            }
        }
        sx += ry;
        ry /= 2; // 가로는 절반으로 줄고
        rx *= 2; // 세로는 2배로 갱신
    }

    move_fish();
}

int solve() {
    int cnt = 0;
    while (!if_end()) {
        cnt++;
        roll();
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    cin >> N >> K;
    board = vector<vector<int>>(N, vector<int>(N, -1));
    for (int i = 0; i < N; ++i) cin >> board[0][i];
    cout << solve();
    return 0;
}

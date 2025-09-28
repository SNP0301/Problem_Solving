#include <iostream>
#include <vector>

using namespace std;

struct student {
    int id;
    int preference[4];
    int x, y;
};

int score[] = {0, 1, 10, 100, 1000};
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    int arr[20][20] = {{0,},};
    vector<student> students(N * N);

    for (int i = 0; i < N * N; i++) {
        cin >> students[i].id;
        for (int j = 0; j < 4; j++) {
            cin >> students[i].preference[j];
        }
    }

    for (int s = 0; s < N * N; s++) {
        int best_x = -1, best_y = -1;
        int best_friend = -1, best_blank = -1;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] != 0) continue;

                int blank_cnt = 0, friend_cnt = 0;
                for (int f = 0; f < 4; f++) { // f of four
                    int nx = i + dx[f];
                    int ny = j + dy[f];
                    if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

                    if (arr[nx][ny] == 0) blank_cnt++;
                    else {
                        for (int k = 0; k < 4; k++) {
                            if (arr[nx][ny] == students[s].preference[k]) {
                                friend_cnt++;
                                break;
                            }
                        }
                    }
                }

                if (friend_cnt > best_friend ||
                    (friend_cnt == best_friend && blank_cnt > best_blank) ||
                    (friend_cnt == best_friend && blank_cnt == best_blank && i < best_x) ||
                    (friend_cnt == best_friend && blank_cnt == best_blank && i == best_x && j < best_y)) {
                        best_x = i;
                        best_y = j;
                        best_friend = friend_cnt;
                        best_blank = blank_cnt;
                }
            }
        }

        arr[best_x][best_y] = students[s].id;
        students[s].x = best_x;
        students[s].y = best_y;
    }

    int ans = 0;
    for (int s = 0; s < N * N; s++) {
        int x = students[s].x;
        int y = students[s].y;

        int friend_cnt = 0;
        for (int f = 0; f < 4; f++) {
            int nx = x + dx[f];
            int ny = y + dy[f];
            if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
            for (int k = 0; k < 4; k++) {
                if (arr[nx][ny] == students[s].preference[k]) {
                    friend_cnt++;
                    break;
                }
            }
        }
        ans += score[friend_cnt];
    }

    cout << ans;

    return 0;
}

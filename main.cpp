/*
    긍정

    문제: 모노미노도미노 https://www.acmicpc.net/problem/20061

    x,y 헷갈림
*/

#include <iostream>
using namespace std;

int answer = 0;
int arr[10][10];

void green_shoot(int t,int x,int y) {
    if (t != 2) {
        while (x+1 < 10 && arr[x+1][y] == 0) x++; // 더 내려갈 수 잇고 빈칸이면
        arr[x][y] = 1;
        if (t == 3) arr[x-1][y] = 1;
    } else {
        while (x+1 < 10 && arr[x+1][y] == 0 && arr[x+1][y+1] == 0) x++;
        arr[x][y] = 1;
        arr[x][y+1] = 1;
    }
}

void blue_shoot(int t,int x,int y) {
    if (t != 3) {
        y += 1;
        while (y+1 < 10 && arr[x][y+1] == 0) y++;
        arr[x][y] = 1;
        if (t == 2) arr[x][y-1] = 1;
    } else {
        while (y+1 < 10 && arr[x][y+1] == 0 && arr[x+1][y+1] == 0) y++;
        arr[x][y] = 1;
        arr[x+1][y] = 1;
    }
}

void green_answer() {
    int cur_ans = 0;
    int cleaned[10] = {0};

    for (int x=4; x<10; x++) {
        int s = arr[x][0]+arr[x][1]+arr[x][2]+arr[x][3];
        if (s == 4) {
            cur_ans += 1;
            cleaned[x] = 1;
            arr[x][0] = arr[x][1] = arr[x][2] = arr[x][3] = 0;
        }
    }
    for (int x=9; x>=4; x--) {
        if (cleaned[x] == 1) {
            for (int nx=x; nx>=4; nx--) {
                if (cleaned[nx] != 1) {
                    for (int y=0; y<4; y++) {
                        arr[x][y] = arr[nx][y];
                        arr[nx][y] = 0;
                    }
                    cleaned[nx] = 1;
                    break;
                }
            }
        }
    }
    answer += cur_ans;
}

void blue_answer() {
    int cur_ans = 0;
    int cleaned[10] = {0};

    for (int y=4; y<10; y++) {
        int s = arr[0][y]+arr[1][y]+arr[2][y]+arr[3][y];
        if (s == 4) {
            cur_ans += 1;
            cleaned[y] = 1;
            arr[0][y] = arr[1][y] = arr[2][y] = arr[3][y] = 0;
        }
    }
    for (int y=9; y>=4; y--) {
        if (cleaned[y] == 1) {
            for (int ny=y; ny>=4; ny--) {
                if (cleaned[ny] != 1) {
                    for (int x=0; x<4; x++) {
                        arr[x][y] = arr[x][ny];
                        arr[x][ny] = 0;
                    }
                    cleaned[ny] = 1;
                    break;
                }
            }
        }
    }
    answer += cur_ans;
}

void green_clean() {
    int to_be_cleaned = 0;
    for (int x=4; x<=5; x++) {
        int s = arr[x][0]+arr[x][1]+arr[x][2]+arr[x][3];
        if (s >= 1) to_be_cleaned += 1;
    }
    for (int x=9; x>=4; x--) {
        for (int y=0; y<4; y++) {
            arr[x][y] = arr[x-to_be_cleaned][y];
        }
    }
}

void blue_clean() {
    int to_be_cleaned = 0;
    for (int y=4; y<=5; y++) {
        int s = arr[0][y]+arr[1][y]+arr[2][y]+arr[3][y];
        if (s >= 1) to_be_cleaned += 1;
    }
    for (int y=9; y>=4; y--) {
        for (int x=0; x<4; x++) {
            arr[x][y] = arr[x][y-to_be_cleaned];
        }
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; 
    if (!(cin >> N)) return 0;

    int t, x, y;
    for (int i=0; i<N; i++) {
        cin >> t >> x >> y;
        green_shoot(t, x, y);
        blue_shoot(t, x, y);
        green_answer();
        blue_answer();
        green_clean();
        blue_clean();
    }

    cout << answer << "\n";
    int cnt = 0;

    for (int i=0; i<10; i++)
        for (int j=0; j<10; j++)
            cnt += arr[i][j];

    cout << cnt << "\n";


    return 0;
}
#include <iostream>
#include <algorithm>

#define MAX_N 100
#define MAX_NUM 3

using namespace std;

int n;
int a[MAX_N], b[MAX_N], c[MAX_N];
int yabawi[MAX_NUM + 1];

int main() {
    cin >> n;

    for(int i = 0; i < n; i++)
        cin >> a[i] >> b[i] >> c[i];

    int max_score = 0;

    // 시작 위치를 전부 가정
    // 그 중 최대 점수를 계산
    for(int i = 1; i <= 3; i++) {
        // 종이컵 전부 비워주기 : 초기화
        yabawi[1] = yabawi[2] = yabawi[3] = 0;

        yabawi[i] = 1;

        int score = 0;

        for(int j = 0; j < n; j++) {
            swap(yabawi[a[j]], yabawi[b[j]]);

            if(yabawi[c[j]])
                score++;
        }

        max_score = max(max_score, score);
    }

    cout << max_score;
    return 0;
}
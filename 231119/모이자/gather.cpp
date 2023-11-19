// 1번째 집으로 모이면 총 이동 거리의 합은 1∗0+2∗1+3∗2+2∗3+6∗4=38이 됩니다.
// 2번째 집으로 모이면 총 이동 거리의 합은 1∗1+2∗0+3∗1+2∗2+6∗3=26이 됩니다.
// 3번째 집으로 모이면 총 이동 거리의 합은 1∗2+2∗1+3∗0+2∗1+6∗2=18이 됩니다.
// 4번째 집으로 모이면 총 이동 거리의 합은 1∗3+2∗2+3∗1+2∗0+6∗1=16이 됩니다.
// 5번째 집으로 모이면 총 이동 거리의 합은 1∗4+2∗3+3∗2+2∗1+6∗0=18이 됩니다.

#include <iostream>
#include <vector>
#include <climits>
#include <cstdlib>

using namespace std;

int n;
int arr[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int answer = INT_MAX;

    for (int i = 0; i < n; i++) {
        int sum_dist = 0;
        for (int j = 0; j < n; j++) {
            sum_dist += abs(j - i) * arr[j];
        }
        answer = min(answer, sum_dist);
    }

    cout << answer;
    return 0;
}
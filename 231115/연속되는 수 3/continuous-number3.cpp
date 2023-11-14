// 연속하는 두 원소의 부호가 같은지 비교하려면 두 원소를 곱해서 판별해보면 된다.

#include <iostream>
#include <algorithm>

#define MAX_N 1000

using namespace std;

int n;
int arr[MAX_N];

int main() {
    // 입력
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    // 연속하여 동일한 부호의 숫자가 나오는 횟수를 구해보며,
    // 그 중 최댓값을 갱신
    int answer = 0, cnt = 0;
    for(int i = 0; i < n; i++) {
        // CASE 1
        if(i >= 1 && arr[i] * arr[i - 1] > 0)
            cnt++;
        // CASE 2
        else
            cnt = 1;

        answer = max(answer, cnt);
    }

    cout << answer;
    return 0;
}
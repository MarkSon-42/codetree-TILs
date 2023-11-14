// 최장 연속 부분 수열

// i가 0이거나 a[i] ≠ a[i - 1]인 경우에 개수를 증가시킨다.

// i = 0인 경우에는 직전 원소를 정의할 수 없으므로, 따로 예외적으로 처리를 해줘야 함!

#include <iostream>
#include <algorithm>

#define MAX_N 1000

using namespace std;

int n;
int arr[MAX_N];

int main() {
    // input
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    // 연속하여 동일한 숫자가 나오는 횟수를 구해보며 - CASE 1
    // 그 중 최댓값을 갱신 - CASE 2
    int answer = 0, cnt = 0;
    for(int i = 0; i < n; i++) {
        // CASE 1
        if(i >= 1 && arr[i] == arr[i - 1])
            cnt++;
        else
            cnt = 1;
        
        answer = max(answer, cnt);
    }

    cout << answer;
    return 0;
}
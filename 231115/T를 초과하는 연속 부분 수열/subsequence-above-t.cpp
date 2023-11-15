#include <iostream>
#include <algorithm>

#define MAX_N 1000

using namespace std;

int n, t;
int arr[MAX_N];

int main() {
    // 입력
    cin >> n >> t;
    for(int i = 0; i < n; i++)
        cin >> arr[i];
    
    // 연속하여 t보다 큰 숫자가 나오는 횟수를 구해보며,
    // 그 중 최댓값을 갱신합니다.
    int ans = 0, cnt = 0;
    for(int i = 0; i < n; i++) {
		// Case 1
        if(arr[i] > t)
            cnt++;
		// Case 2
        else
            cnt = 0;
        
        ans = max(ans, cnt);
    }
    
    cout << ans;
    return 0;
}
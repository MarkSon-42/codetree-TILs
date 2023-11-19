#include <iostream>
#include <climits>

#define MAX_N 1000000

using namespace std;
// int Fibbo(int n) {
//     if(memo[n] != -1)          // 이미 n번째 값을 구해본 적이 있다면
//         return memo[n];        // memo에 적혀있는 값을 반환해줍니다.
//     if(n <= 2)                 // n이 2이하인 경우에는 종료 조건이므로 
//         memo[n] = 1;           // 해당하는 숫자를 memo에 넣어줍니다.
//     else                       // 종료조건이 아닌 경우에는 
//         memo[n] = Fibbo(n - 1) + Fibbo(n - 2);  // 점화식을 이용하여 답을 구한 뒤
//                                                 // 해당 값을 memo에 저장해줍니다.
//     return memo[n];                             // memo 값을 반환합니다.
// }



int main() {

    int n;
    cin >> n;
    int dp[MAX_N] = {};

    dp[1] = 1;
    dp[2] = 1;

    for(int i = 3; i <= n; i++)
        dp[i] = dp[i - 1] + dp[i - 2];

    cout << dp[n];

    return 0;
}
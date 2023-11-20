#include <iostream>

#define MAX_N 1000

using namespace std;



int main() {
    int n;
    cin >> n;
    int dp[MAX_N + 1] = {};
    dp[1] = 2;
    dp[2] = 7;

    for (int i = 3; i <= n; i++) {
        dp[i] = ((dp[i - 1] * 3) + 1) % 1000000007;
    }

    cout << dp[n];
    return 0;
}
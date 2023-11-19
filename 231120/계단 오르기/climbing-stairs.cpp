#include <iostream>
#include <climits>

#define MAX_N 1000000

using namespace std;


int main() {

    int n;
    cin >> n;
    int dp[MAX_N] = {};

    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    dp[4] = 1;

    for(int i = 5; i <= n; i++)
            dp[i] = dp[i - 2] + dp[i - 4];

    cout << dp[n] % 10007;

    return 0;
}
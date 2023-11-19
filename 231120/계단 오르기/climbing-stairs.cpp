#include <iostream>

#define MAX_N 100000

using namespace std;


int main() {

    int n;
    cin >> n;
    int dp[MAX_N] = {};
    
    dp[0] = 0;
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;

    for(int i = 4; i <= n; i++)
            dp[i] = dp[i - 2] + dp[i - 3];

    cout << dp[n] % 10007;

    return 0;
}
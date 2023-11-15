#include <iostream>
#include <vector>

#define MAX_T 1000000

using namespace std;

int n, m;
vector<int> pos_a(MAX_T + 1, 0);  // Using vectors instead of arrays for A's positions
vector<int> pos_b(MAX_T + 1, 0);  // Using vectors instead of arrays for B's positions

int main() {
    // input
    cin >> n >> m;

    // Record where A is standing every second
    int time_a = 1;
    for (int i = 0; i < n; i++) {
        char d;
        int t;
        cin >> d >> t;

        while (t--) {
            if (d == 'R')
                pos_a[time_a] = pos_a[time_a - 1] + 1;
            else
                pos_a[time_a] = pos_a[time_a - 1] - 1;

            time_a++;
        }
    }

    // Record where B is standing every second
    int time_b = 1;
    for (int i = 0; i < m; i++) {
        char d;
        int t;
        cin >> d >> t;

        while (t--) {
            if (d == 'R')
                pos_b[time_b] = pos_b[time_b - 1] + 1;
            else
                pos_b[time_b] = pos_b[time_b - 1] - 1;

            time_b++;
        }
    }

    // Find the time of first meeting.
    int ans = -1;
    for (int i = 1; i < time_a; i++) {
        if (pos_a[i] == pos_b[i]) {
            ans = i;
            break;
        }
    }

    cout << ans;
    return 0;
}
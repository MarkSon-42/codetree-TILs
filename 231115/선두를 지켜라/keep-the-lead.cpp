#include <iostream>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    int A_speed, A_time, B_speed, B_time, changes = 0;

    for (int i = 0; i < N; ++i) {
        cin >> A_speed >> A_time;
    }

    for (int i = 0; i < M; ++i) {
        cin >> B_speed >> B_time;
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if ((A_speed > B_speed && A_time <= B_time) ||
                (A_speed < B_speed && A_time >= B_time)) {
                ++changes;
            }
        }
    }

    cout << changes << endl;

    return 0;
}
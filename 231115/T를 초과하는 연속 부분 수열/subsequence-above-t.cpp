//
// Created by Mac Apple on 2023/11/15.
//
#include <iostream>
#include <vector>

using namespace std;

#define MAX_ 1000

int main() {
    int n, t;
    cin >> n >> t;

    vector<int> sequence(n);

    for (int i = 0; i < n; i++) {
        cin >> sequence[i];
    }

    int maxLength = 0;
    int currentLength = 0;

    for (int i = 0; i < n; i++) {
        if (sequence[i] > t)
            currentLength++;
        else {
            maxLength = max(maxLength, currentLength);
            currentLength = 0;
        }
    }

    maxLength = max(maxLength, currentLength);

    cout << maxLength;

    return 0;
}
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <climits>

using namespace std;

int n = 5;
int arr[5] = {1, 5, 2, 6, 8};

int main() {
    int max_sum = 0;
    for (int i = 0; i < n; i++) {
        arr[i] *= 2;

        int sum_diff = 0;
        for (int j = 0; j < n - 1; j++) {
            sum_diff += abs(arr[j + 1] - arr[j]);
        }

        max_sum = max(max_sum, sum_diff);
        arr[i] /= 2;
    }
    cout << max_sum;

    int neg_arr[5] = {-6, -5, -2, -10, 15};
    
    int max_val = INT_MIN;
    for (int i = 0; i < n; i++) {
        if (neg_arr[i] > max_val)
            max_val = arr[i];
    }
    
    int min_val = INT_MAX;
    for (int i = 0; i < n; i++) {
        if (neg_arr[i] < min_val)
            min_val = neg_arr[i];
    }
    
    cout << max_val << " " << min_val;
    
    
    return 0;
}
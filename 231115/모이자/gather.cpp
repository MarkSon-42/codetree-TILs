#include <iostream>
#include <climits>
using namespace std;

int n = 5;
int arr[5] = {-6, -5, -2, -10, -15};

int main() {
    int max_val = INT_MIN;
    for(int i = 0; i < n; i++)
        if(arr[i] > max_val)
            max_val = arr[i];
    
    int min_val = INT_MAX;
    for(int i = 0; i < n; i++)
        if(arr[i] < min_val)
            min_val = arr[i];
    
    cout << max_val << " " << min_val;
    
    return 0;
}

>> -2 -15
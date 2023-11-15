#include <iostream>

using namespace std;

int main() {
    // 배열을 구현합니다.
	int arr[10];
	
	// 10개의 정수를 입력받습니다.
	for(int i = 0; i < 10; i++) {
		cin >> arr[i];
	}
	
	int max_val = arr[0];
	
	// 10개의 숫자들 중 최댓값을 구합니다.
	for(int i = 1; i < 10; i++) {
		if(arr[i] > max_val)
			max_val = arr[i];
	}
	
    // 최댓값을 출력합니다.
    cout << max_val;

    return 0;
}
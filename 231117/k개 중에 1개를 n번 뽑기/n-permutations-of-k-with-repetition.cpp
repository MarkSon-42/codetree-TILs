#include <iostream>
#include <vector>

using namespace std;

int k, n;
vector<int> selected_nums;

// 선택된 원소들을 출력해줍니다.
void PrintPermutation() {
    for(int i = 0; i < (int) selected_nums.size(); i++)
        cout << selected_nums[i] << " ";
    cout << endl;
}

void FindPermutations(int cnt) {
    // n개를 모두 뽑은 경우 답을 출력해줍니다.
    if(cnt == n) {
        PrintPermutation();
        return;
    }

    // 1부터 k까지의 각 숫자가 뽑혔을 때의 경우를 탐색합니다.
    for(int i = 1; i <= k; i++) {
        selected_nums.push_back(i);
        FindPermutations(cnt + 1);
        selected_nums.pop_back();
    }
}

int main() {
    cin >> k >> n;
    
    FindPermutations(0);
    return 0;
}
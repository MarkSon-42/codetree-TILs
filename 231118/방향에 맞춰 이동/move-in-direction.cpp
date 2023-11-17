// (x, y)위치에서 시작해서 한 칸 이동
// dir이 방향을 알려준다 생각하면 됨.


// 숫자 0 -> 오른쪽
// 숫자 1 -> 아래쪽
// 숫자 2 -> 왼쪽
// 숫자 3 -> 위쪽

// 시계방향

dir_num = 2  // 왼쪽으로 이동
x, y = 1, 1

if dir_num == 0:
    nx, ny = x + 1, y
elif dir_num == 1:
    nx, ny = x, y - 1


// 특정 방향에 대해 이동하는 경우에는 dx, dy 테크닉을 많이 사용!

dir_num = 2 
x, y = 1, 5
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

nx, ny = x + dx[dir_num], y + dy[dir_num]




#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    return 0;
}
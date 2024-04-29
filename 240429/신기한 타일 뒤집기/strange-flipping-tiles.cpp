#include <iostream>

using namespace std;

#define MAX_K 100000

int n;
int a[2 * MAX_K + 1];
int b, w;

int main() {
    // 변수 입력
    cin >> n;

    int cur = MAX_K;

    int x;
    char c;

    for(int i = 0; i < n; i++) {
        
        cin >> x >> c;
        if(c == 'L') {
            // x칸 왼쪽으로 칠합니다.
            while(x--) {
                a[cur] = 1;
                if(x) cur--;
            }
        }
        else {
            // x칸 오른쪽으로 칠합니다.
            while(x--) {
                a[cur] = 2;
                if(x) cur++;
            }
        }
    }

    for(int i = 0; i <= 2 * MAX_K; i++) {
        if(a[i] == 1) w++;
        if(a[i] == 2) b++;
    }

    // 정답을 출력합니다.
    cout << w << " " << b;
    return 0;
}
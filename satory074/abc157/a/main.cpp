#include <iostream>
using namespace std;

int main() {
	int a;
    cin >> a;
	
    int ans = a / 2;
    ans += a - ans * 2;

    cout << ans << endl;
}

#include <cstdio>
using namespace std;
int main() {
	int n, m;
	scanf("%d %d", &n, &m);

    int sc[m][2];
    int s, c;
    for (int i=0; i < m; i++){
        scanf("%d %d", &s, &c);
        sc[i][0] = s;
        sc[i][1] = c;
    }

    for (int i=0; i < m; i++){
        printf("%d %d\n", sc[i][0], sc[i][1]);
    }
}

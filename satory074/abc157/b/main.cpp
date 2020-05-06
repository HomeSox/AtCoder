#include <cstdio>
using namespace std;
int main() {
    // yoko
	int yoko[3][3];
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            scanf("%d", &yoko[i][j]);
        }
    }

    // tate
    int tate[3][3];
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            tate[i][j] = yoko[j][i]
        }
    }

    // naname
    int naname[2][3];
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++){
            naname[i][j] = yoko[j][j]
        }
    }


    int line[8][3];

    int
}

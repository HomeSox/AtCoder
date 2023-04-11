package main

import (
	"fmt"
)

func main() {
	var A, B, C, D int
	fmt.Scan(&A, &B, &C, &D)

	var ans string

	if A > C {
		ans = "Aoki"
	} else if A < C {
		ans = "Takahashi"
	} else {
		if B > D {
			ans = "Aoki"
		} else {
			ans = "Takahashi"
		}
	}

	fmt.Println(ans)
}

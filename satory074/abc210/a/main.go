package main

import (
	"fmt"
)

func main() {
	var N, A, X, Y int

	fmt.Scan(&N, &A, &X, &Y)

	var ans int
	ans = 0

	for i := 1; i <= N; i++ {
		if i <= A {
			ans += X
		} else {
			ans += Y
		}
	}

	fmt.Println(ans)
}

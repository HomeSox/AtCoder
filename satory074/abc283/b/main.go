package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)

	var A []int
	for i := 0; i < N; i++ {
		var a int
		fmt.Scan(&a)
		A = append(A, a)
	}

	var Q int
	fmt.Scan(&Q)

	for i := 0; i < Q; i++ {
		var q int
		fmt.Scan(&q)

		if q == 1 {
			var k, x int
			fmt.Scan(&k)
			fmt.Scan(&x)

			A[k-1] = x

			continue
		}

		if q == 2 {
			var k int
			fmt.Scan(&k)

			fmt.Println(A[k-1])

			continue
		}
	}
}

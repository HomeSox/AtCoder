package main

import (
	"fmt"
	"math"
)

func main() {
	var N int
	fmt.Scan(&N)

	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}

	minus := 0

	for i := 0; i < N; i++ {
		if A[i] < 0 {
			minus++
		}
	}

	var ans int64 = 0
	for i := 0; i < N; i++ {
		ans += int64(math.Abs(float64(A[i])))
	}

	if minus%2 != 0 {
		mi := math.MaxInt32
		for i := 0; i < N; i++ {
			mi = int(math.Min(float64(mi), math.Abs(float64(A[i]))))
		}

		ans -= int64(mi) * 2
	}

	fmt.Println(ans)
}

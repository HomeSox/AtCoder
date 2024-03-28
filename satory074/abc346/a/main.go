package main

import (
	"fmt"
)

func main() {
	var N int
	var A []int

	fmt.Scan(&N)
	for i := 0; i < N; i++ {
		var a int
		fmt.Scan(&a)
		A = append(A, a)
	}

	// Ai * Ai+1を計算
	var B []int
	for i := 0; i < N-1; i++ {
		B = append(B, A[i]*A[i+1])
	}

	// 空白区切りで出力
	for i := 0; i < N-1; i++ {
		fmt.Printf("%d ", B[i])
	}
}

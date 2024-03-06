package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)

	// 4桁で0埋めした文字列を作成
	s := fmt.Sprintf("%04d", N)
	fmt.Println(s)
}

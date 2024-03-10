package main

import (
	"fmt"
	"strings"
)

func main() {
	var S string

	fmt.Scan(&S)

	// Sを空白で分割して配列に格納
	sp := strings.Split(S, "|")

	fmt.Println(sp[0] + sp[2])

}

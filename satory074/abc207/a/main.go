package main

import (
	"fmt"
	"sort"
)

func main() {
	var A, B, C int
	fmt.Scan(&A, &B, &C)

	l := []int{A, B, C}
	sort.Sort(sort.Reverse(sort.IntSlice(l)))

	fmt.Println(l[0] + l[1])
}

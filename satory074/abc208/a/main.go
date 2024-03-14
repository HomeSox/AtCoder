package main

import (
	"fmt"
)

func main() {
	var A, B int
	fmt.Scan(&A, &B)

	if A <= B && B <= A*6 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}

package main

import (
	"fmt"
)

func main() {
	var X int
	fmt.Scan(&X)

	if X%100 == 0 && X != 0 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}

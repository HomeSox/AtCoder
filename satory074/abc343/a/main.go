package main

import (
	"fmt"
	"os"
)

func main() {
	var A, B int
	fmt.Scan(&A, &B)

	for i := 0; i < 10; i++ {
		if i != A+B {
			fmt.Println(i)
			os.Exit(0)
		}
	}
}

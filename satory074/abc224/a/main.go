package main

import (
	"fmt"
)

func main() {
	var S string
	fmt.Scan(&S)

	tail := S[len(S)-2:]

	if tail == "st" {
		fmt.Println("ist")
	} else {
		fmt.Println("er")
	}
}

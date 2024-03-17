package main

import (
	"fmt"
)

func main() {
	var S string
	fmt.Scan(&S)

	if S[0] != '<' {
		fmt.Println("No")
		return
	}

	if S[len(S)-1] != '>' {
		fmt.Println("No")
		return
	}

	for i := 1; i < len(S)-1; i++ {
		if S[i] != '=' {
			fmt.Println("No")
			return
		}
	}

	fmt.Println("Yes")
}

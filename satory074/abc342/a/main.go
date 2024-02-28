package main

import (
	"fmt"
)

func main() {
	var S string
	fmt.Scan(&S)

	var ans int

	if S[0] != S[1] {
		if S[0] == S[2] {
			ans = 2
		} else {
			ans = 1
		}
	} else {
		for i := 2; i < len(S); i++ {
			if S[i] != S[0] {
				ans = i + 1
				break
			}
		}
	}

	fmt.Println(ans)
}

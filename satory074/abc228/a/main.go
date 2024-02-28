package main

import (
	"fmt"
)

func main() {
	var S, T, X int
	fmt.Scan(&S, &T, &X)

	if S > T {
		for i := S; i < 24; i++ {
			if i == X {
				fmt.Println("Yes")
				return
			}
		}

		for i := 0; i < T; i++ {
			if i == X {
				fmt.Println("Yes")
				return
			}
		}

		fmt.Println("No")
		return
	} else {
		for i := S; i < T; i++ {
			if i == X {
				fmt.Println("Yes")
				return
			}
		}

		fmt.Println("No")
		return
	}
}

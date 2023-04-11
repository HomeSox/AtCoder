package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	s, _ := reader.ReadString('\n')
	s = strings.TrimSpace(s)

	converted := convertString(s)
	fmt.Println(converted)
}

func convertString(s string) string {
	return strings.ReplaceAll(s, ",", " ")
}

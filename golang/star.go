package main

import (
	"fmt"
)

func main() {
	n := 5 // Number of rows
	for i := 1; i <= n; i++ {
		for j := 1; j <= i; j++ {
                fmt.Println("* ")
}
		fmt.Println("\n" )
	}
}

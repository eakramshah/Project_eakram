package main

import (
	"fmt"
	"reflect"
)

func main() {

	var grades int = 67
	var message string = "Hello World"
	fmt.Printf("variable: %v \n", reflect.TypeOf(10000))
	fmt.Printf("variable: %v \n", reflect.TypeOf("Sheeba"))
	fmt.Printf("variable: %v \n", reflect.TypeOf(10.5))
	fmt.Printf("variable: %v \n", reflect.TypeOf(true))
	fmt.Printf("variable: %v \n", reflect.TypeOf(grades))
	fmt.Printf("variable: %v \n", reflect.TypeOf(message))

}

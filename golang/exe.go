package main

import (
	"fmt"
	"os/exec"
)

func main() {
	// Define the command
	cmd := exec.Command("sh", "-c", "echo $SHELL && echo Hello from Golang!")

	// Run the command and capture the output
	output, err := cmd.Output()
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	// Print the output
	fmt.Println(string(output))
}

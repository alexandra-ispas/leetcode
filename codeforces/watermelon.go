package main

import "fmt"

func main() {
	var i int
	_, err := fmt.Scanf("%d", &i)
	if err != nil {
		fmt.Println("could not read integer from input")
		return
	}

	if i <= 2 {
		fmt.Println("NO")
		return
	}

	if i%2 == 0 {
		fmt.Println("YES")
		return
	}

	fmt.Println("NO")
	return
}

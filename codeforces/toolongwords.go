package main

import "fmt"

const maxLineSize = 10

func abbreviate(line string) string {
	return fmt.Sprintf("%c%d%c", line[0], len(line)-2, line[len(line)-1])
}

func main() {
	var n int
	_, err := fmt.Scanf("%d\n", &n)
	if err != nil {
		fmt.Println("could not read integer from input")
		return
	}

	var line string
	for i := 0; i < n; i++ {
		_, err := fmt.Scanf("%s\n", &line)
		if err != nil {
			fmt.Println("could not read line from input")
			return
		}

		if len(line) > maxLineSize {
			line = abbreviate(line)
		}

		fmt.Println(line)
	}
}

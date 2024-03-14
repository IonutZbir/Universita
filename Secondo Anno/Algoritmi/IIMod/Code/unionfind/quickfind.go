package main

import "fmt"

type Node struct {
	Root *Node
	Val  int
}

type Set struct {
	Elems []Node
	size  int
}

func main() {
	fmt.Println("vim-go")
}

package main

import (
	_ "fmt"
)

type Node struct {
	Root *Node
	Val  int
}

type Set struct {
	Elems []Node
	Size  int
}

type UnionFind struct {
	Data []Set
}

func (nd Node) Init(val int) *Node {
	return &Node{
		Root: nil,
		Val:  val,
	}
}

func (s Set) Init() *Set {
	return &Set{
		Elems: make([]Node, 0),
		Size:  0,
	}
}

func (uf *UnionFind) MakeSet() {

}

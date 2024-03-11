package data_struct

import "fmt"

type Node struct {
	Key int
	Val int
}

type DHeap struct {
	Data     []Node
	Type     int
	HeapSize int
}

func (n Node) Init(key, val int) *Node {
	return &Node{
		Key: key,
		Val: val,
	}
}

func (h DHeap) Init(tp int) *DHeap {
	return &DHeap{
		Data:     make([]Node, 0),
		Type:     tp,
		HeapSize: 0,
	}
}

func (h *DHeap) swap(i, j int) {
	h.Data[i], h.Data[j] = h.Data[j], h.Data[i]
}

func (h *DHeap) minChild(nd int) int {
	minC := h.Child(nd, 0)
	for i := 1; i < h.Type; i++ {
		j := h.Child(nd, i)
		if j < 0 {
			break
		}
		if h.Data[minC].Key > h.Data[j].Key {
			minC = j
		}
	}
	return minC
}

func (h *DHeap) Child(i, j int) int {
	// return the jth child of i
	k := (h.Type * i) + j
	if k < h.HeapSize {
		return k
	}
	return -1
}

func (h *DHeap) Parent(i int) int {
	return (i - 1) / h.Type
}

func (h *DHeap) MoveHigh(index int) {
	for i := index; i >= 0; i-- {
		nd := h.Data[i]
		j := h.Parent(i)
		if j < 0 {
			break
		}
		parent := h.Data[j]

		if nd.Key < parent.Key {
			h.swap(i, j)
		}
	}
}

func (h *DHeap) MoveDown(index int) {
	for i := index; i < h.HeapSize; {
		minC := h.minChild(i)
		if minC != -1 && h.Data[minC].Key < h.Data[i].Key {
			h.swap(i, minC)
			i = minC
		} else {
			break
		}
	}
}

func (h *DHeap) FindMin() *Node {
	if h.HeapSize > 0 {
		return &h.Data[0]
	}
	return nil
}

func (h *DHeap) Insert(key, val int) {
	h.Data = append(h.Data, *Node{}.Init(key, val))
	h.HeapSize++
	h.MoveHigh(h.HeapSize - 1)
}

func (h *DHeap) IncreaseKey(index int, delta int) {
	nd := &h.Data[index]
	nd.Key = nd.Key + delta
	h.MoveDown(index)
}

func (h *DHeap) DecreaseKey(index int, delta int) {
	if index < h.HeapSize {
		nd := &h.Data[index]
		nd.Key = nd.Key - delta
		h.MoveHigh(index)
	}
}

func (h *DHeap) ToString() {
	fmt.Printf("[")
	i := 0
	for ; i < h.HeapSize-1; i++ {
		fmt.Printf("(Key: %v, Val: %v),", h.Data[i].Key, h.Data[i].Val)
	}
	fmt.Printf("(Key: %v, Val: %v)\n", h.Data[i].Key, h.Data[i].Val)
}

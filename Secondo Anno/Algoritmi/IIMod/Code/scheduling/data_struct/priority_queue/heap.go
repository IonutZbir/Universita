package heap

type Node struct {
	Key int
	Val int
}

type DHeap struct {
	Data []Node
	Type int
	HeapSize int
}

func (hp DHeap) swap(i, j int) {
	hp.Data[i], hp.Data[j] = hp.Data[j], hp.Data[i]
}

func (hp DHeap) minChild(nd int) int{
	minC := hp.Child(nd, 0)
	for i := 1; i < hp.Type; i++ {
		j := hp.Child(nd, i)
		if j < 0 {
			break;
		}
		if hp.Data[minC].Key > hp.Data[j].Key{
			minC = j
		}
	}
	return minC
}

func (Node) Init(key, val int) *Node {
	return &Node{
		Key: key,
		Val: val,
	}
}

func (DHeap) Init(tp int) *DHeap {
	return &DHeap{
		Data: make([]Node, 0),
		Type: tp,
		HeapSize: 0,
	}
}

func (hp DHeap) Child(i, j int) int {
	// return the jth child of i
	k := (hp.Type * i) + j
	if k < hp.HeapSize {
		return k
	}
	return -1
}

func (hp DHeap) Parent(i int) int {
	return (i - 1) / hp.Type
}

func (hp DHeap) moveHigh(index int) {
	for i := index; i > 0; i-- {
		nd := hp.Data[i]
		j := hp.Parent(i)
		parent := hp.Data[j]

		if nd.Key < parent.Key {
			hp.swap(i, j)
		}
	}
}

func (hp DHeap) moveDown(index int) {
	for i := index; i < hp.HeapSize; i++ {
		minC := hp.minChild(i)
		if minC != -1 {
			hp.swap(i, minC)	
		}
	}
}





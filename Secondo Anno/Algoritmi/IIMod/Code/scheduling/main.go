package main

import (
	"fmt"
	"math/rand"
	"sched/algo"
	ds "sched/data_struct"
)

func main() {
	t := ds.Tasks{}.Init()
	for i := 0; i < 10; i++ {
		start := rand.Float32() * 50.0
		finish := rand.Float32() * 100.0
		if finish < start {
			c := start
			start = finish
			finish = c
		}
		t.Data = append(t.Data, *ds.Task{}.Init(start, finish))
	}

	schedule := algo.IntervalPart(t)
	fmt.Println()
	
	for _, sched := range schedule {
		sched.ToString()
	}

}

func main1() {
	hp := ds.DHeap{}.Init(5)

	for i := 0; i < 10; i++ {
		j := rand.Intn(100)
		val := i
		key := j
		hp.Insert(float32(key), float32(val))
	}

	hp.ToString()

	m := hp.FindMin()
	m.ToString()
	hp.PrintTree()

	hp.Delete(4)

	hp.DeleteMin()

	hp.ToString()

	hp.PrintTree()

}

package main

import (
	"fmt"
	"math/rand"
	"sched/algo"
	ds "sched/data_struct"
)

func main2() {
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

	sched := algo.IntervalScheduling(t)
	sched.ToString()
}

func main() {
	hp := ds.DHeap{}.Init(3)

	for i := 0; i < 10; i++ {
		j := rand.Intn(100)
		hp.Insert(j, i)
	}

	fmt.Println(hp.FindMin())
	hp.ToString()
	//hp.PrintTree()
}

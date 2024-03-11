package main

import (
	"math/rand"
	"sched/algo"
	task "sched/data_struct"
)

func main() {
	t := task.Tasks{}.Init()
	for i := 0; i < 10; i++ {
		start := rand.Float32() * 50.0
		finish := rand.Float32() * 100.0
		if finish < start {
			c := start
			start = finish
			finish = c
		}
		t.Data = append(t.Data, *task.Task{}.Init(start, finish))
	}

	sched := algo.IntervalScheduling(t)
	sched.ToString()
}

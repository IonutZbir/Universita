package main

import(
	"fmt"
	"sort"
)

type Task struct{
	start	float64
	finish	float64
}

type Tasks struct{
	data	[]Task
}

func (t Tasks) Init() *Tasks{
	return &Tasks{
		data: make([]Task, 0),
	}
}

func (t Task) Init(start float64, finish float64) *Task{
	return &Task{
		start: start,
		finish: finish,
	}
}

func (t Task) IsCompatible(t1 Task) bool {
	return t.start >= t1.finish
}

func IntervalScheduling(intervals *Tasks) Tasks  {
	
	// ordino per finish time
	sort.Slice(intervals.data, func(i, j int) bool{
		return intervals.data[i].finish < intervals.data[j].finish
	})

	lenght := len(intervals.data)

	schedule := Tasks{}.Init()
	fmt.Println(*intervals)

	tasks := intervals.data 
	last := 0
	schedule.data = append(schedule.data, tasks[last])

	for i := 1; i < lenght ; i++ {
		if(tasks[i].IsCompatible(tasks[last])){
			schedule.data = append(schedule.data, tasks[i])
			last = i
		}
	}
	return *schedule
}

func main() {
	
	t := Tasks{}.Init()
	for i := 0; i < 10; i++ {
		t.data = append(t.data, *Task{}.Init(float64(i) * 1.32, float64(i) * 1.42))
	}
	t.data[0].start = 1.43
	t.data[0].finish = 5.01

	sched := IntervalScheduling(t)
	fmt.Println(sched)

}

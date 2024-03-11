package task

import "fmt"

type Task struct {
	Start  float32
	Finish float32
}

type Tasks struct {
	Data []Task
}

func (Tasks) Init() *Tasks {
	return &Tasks{
		Data: make([]Task, 0),
	}
}

func (Task) Init(start float32, finish float32) *Task {
	return &Task{
		Start:  start,
		Finish: finish,
	}
}

func (t Task) IsCompatible(t1 Task) bool {
	return t.Start >= t1.Finish
}

func (t Task) ToString() {
	fmt.Printf("(%0.2v s, %0.2v s)", t.Start, t.Finish)
}

func (i Tasks) ToString() {
	fmt.Print("[")
	for _, t := range i.Data {
		t.ToString()
	}
	fmt.Println("]")
}

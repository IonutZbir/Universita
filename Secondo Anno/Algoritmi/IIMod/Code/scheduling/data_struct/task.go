package task

type Task struct{
	Start	float64
	Finish	float64
}

type Tasks struct{
	Data	[]Task
}

func (Tasks) Init() *Tasks{
	return &Tasks{
		Data: make([]Task, 0),
	}
}

func (Task) Init(start float64, finish float64) *Task{
	return &Task{
		Start: start,
		Finish: finish,
	}
}

func (t Task) IsCompatible(t1 Task) bool {
	return t.Start >= t1.Finish
}


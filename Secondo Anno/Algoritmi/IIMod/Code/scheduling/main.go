package	main

import(
	"fmt"
	"sched/algo"
	"sched/data_struct"
)

func smain() {
	
	t := task.Tasks{}.Init()
	for i := 0; i < 10; i++ {
		t.Data = append(t.Data, *task.Task{}.Init(float64(i) * 1.32, float64(i) * 1.42))
	}
	t.Data[0].Start = 1.43
	t.Data[0].Finish = 5.01

	sched := algo.IntervalScheduling(t)
	fmt.Println(sched)

}


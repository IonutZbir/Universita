package algo

import (
	_"fmt"
	ds "sched/data_struct"
	"sort"
)

func IntervalPart(intervals *ds.Tasks) []ds.Tasks {
	schedule := make([]ds.Tasks, 0)
	pq := ds.DHeap{}.Init(2)

	sort.Slice(intervals.Data, func (i, j int) bool {
		return intervals.Data[i].Start < intervals.Data[j].Start
	})

	tasks := intervals.Data
	length := len(tasks)

	cl := 0
	pq.Insert(tasks[0].Finish, 0)
	schedule = append(schedule, *ds.Tasks{}.Init())

	for i := 0; i < length; i++ {
		task := tasks[i]
		//task.ToString()
		//fmt.Println()
		m := pq.FindMin().Key
		//fmt.Println("[INFO]: MIN:", m)
		if(task.Start >= m){
			delta := task.Finish - pq.Data[0].Key
			pq.IncreaseKey(cl, delta)
			schedule[cl].Data = append(schedule[cl].Data, task)
		}else {
			pq.Insert(task.Finish, 0)
			schedule = append(schedule, *ds.Tasks{}.Init())
			schedule[cl].Data = append(schedule[cl].Data, task)
			cl++
		}
	}

	pq.PrintTree()
	
	return schedule
}

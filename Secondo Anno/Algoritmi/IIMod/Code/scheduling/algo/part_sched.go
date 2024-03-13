package algo

import (
	"fmt"
	_ "fmt"
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

	pq.Insert(tasks[0].Finish, tasks[0])


	for i := 1; i < length; i++ {
		task := tasks[i]
		//task.ToString()
		//fmt.Println()
		m := pq.FindMin().Key
		pq.PrintTree()
		fmt.Println()
		if(task.Start >= m){
			fmt.Printf("[INFO]: %v >= %v? = %v\n", task.Start, m, task.Start >= m)
			delta := task.Finish - pq.Data[0].Key
			pq.Data[0].Val.Data = append(pq.Data[0].Val.Data, task)
			pq.IncreaseKey(0, delta)
		}else {
			pq.Insert(task.Finish, task)
		}
	}

	pq.PrintTree()
	nds := 0
	for i := 0; i < pq.HeapSize; i++ {
		fmt.Printf("\n%v == %v = %v\n", nds, pq.HeapSize - 1, nds == pq.HeapSize - 1)
		if nds == pq.HeapSize - 1{
			break;	
		}
		nd := pq.Data[i]
		for j := 0;  j < len(nd.Val.Data);  j++ {
			schedule = append(schedule, *ds.Tasks{}.Init())
			schedule[i].Data = append(schedule[i].Data, nd.Val.Data[j])
			nds++
			fmt.Println(nds)
		}
	
	}

	fmt.Println(schedule)

	return schedule
}

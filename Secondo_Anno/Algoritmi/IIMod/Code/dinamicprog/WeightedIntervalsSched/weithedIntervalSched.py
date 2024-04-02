import random, time


class Job:
    def __init__(self, start, finish, weight: int) -> None:
        self.start = start
        self.finish = finish
        self.weight = weight

    def is_compatible(self, job) -> bool:
        return self.start >= job.finish

    def to_string(self):
        return (self.start, self.finish, self.weight)


def print_intervals(intervals: list[Job]):
    print("[INFO]:", end="")
    for j in intervals:
        print(j.to_string(), end=",")
    print()


def binary_search(arr: list[Job], job_index: int, s, f: int) -> int:
    if s > f:
        return -1

    m = (s + f) // 2
    if arr[m].finish <= arr[job_index].start:
        return max(m, binary_search(arr, job_index, m + 1, f))
    else:
        return binary_search(arr, job_index, s, m - 1)


def compute_p(arr: list[Job]) -> list[int]:
    p = []
    n = len(arr)
    for i in range(n):
        j = binary_search(arr, i, 0, n)
        p.append(j)
    return p


def create_intervals(n: int) -> list[Job]:
    i = []

    for _ in range(n):

        j = random.randint(1, 100)
        l = random.randint(1, 100)
        random.seed(time.time_ns())
        s = (random.random() % 50) + j
        f = (random.random() % 50) + l
        w = random.randint(abs(l - j) // 2, abs(l + j))
        s = f"{s:.3f}"
        f = f"{f:.3f}"

        s = f if s > f else s

        i.append(Job(s, f, w))

    return i


def compute_OPT(intervals: list[Job], p: list[int]) -> list[int]:
    n = len(intervals)
    OPT = [0] * n

    print("UNORDERED")
    print_intervals(intervals)

    intervals = sorted(intervals, key=lambda x: x.finish)

    print("ORDERED")
    print_intervals(intervals)

    print(p)

    OPT[0] = 0
    for i in range(1, n):
        OPT[i] = max(OPT[i - 1], intervals[i].weight + OPT[p[i]])

    return OPT


def find_solution(OPT, p: list[int], intervals: list[Job], i: int):
    print(i)
    if i == 0:
        return []
    elif intervals[i].weight + OPT[p[i]] > OPT[i - 1]:
        return [i] + find_solution(OPT, p, intervals, p[i])
    else:
        return find_solution(OPT, p, intervals, i - 1)


def weighted_intervals_sched(intervals) -> tuple[int, list[int]]:
    n = len(intervals)
    p = compute_p(intervals)
    OPT = compute_OPT(intervals, p)
    SOL = find_solution(OPT, p, intervals, n - 1)

    return OPT[n - 1], SOL


intervals = create_intervals(5)

intervals2 = [
    Job(1, 4, 1),
    Job(4, 7, 4),
    Job(3, 5, 2),
    Job(4, 11, 8),
    Job(5, 9, 6),
    Job(3, 8, 5),
    Job(0, 6, 3),
    Job(6, 10, 7),
]

OPT, SOL = weighted_intervals_sched(intervals)
print(["[INFO]: Il valore della soluzione ottima è: ", OPT])
print("[INFO]: La soluzione ottima è: ", SOL)

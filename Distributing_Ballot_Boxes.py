import sys
# Does not pass all test cases, fails test 67 for time limit exceeded

class Heap:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.Heap = [[0, 0, 0]] * (self.maxSize + 1)

    def insert(self, node):
        self.size += 1
        self.Heap[self.size] = node
        self.swim(self.size)

    def swim(self, k):
        temp = self.Heap[k]
        while k > 1 and self.Heap[k // 2][1] < temp[1]:
            self.Heap[k] = self.Heap[k // 2]
            k = k // 2
        self.Heap[k] = temp

    def sink(self):
        k = 1
        temp = self.Heap[k]
        while 2 * k <= self.size:
            j = 2 * k
            if j < self.size and self.Heap[j][1] < self.Heap[j + 1][1]:
                j += 1
            if not temp[1] < self.Heap[j][1]:
                break
            self.Heap[k] = self.Heap[j]
            k = j
        self.Heap[k] = temp

    def min(self):
        return self.Heap[1]

    def __str__(self):



info = sys.stdin.readline().split()
while info != ["-1", "-1"]:
    info = [int(i) for i in info]
    cities = Heap(info[0])
    for i in range(info[0]):
        pop = int(sys.stdin.readline())
        cities.insert([1, pop, pop])
    info[1] -= info[0]

    while info[1] > 0:
        # Calculate new population per ballot box
        if cities.min()[2] % (cities.min()[0] + 1) != 0:
            cities.min()[1] = int(cities.min()[2] // (cities.min()[0] + 1) + 1)
        else:
            cities.min()[1] = cities.min()[2] // (cities.min()[0] + 1)
        cities.min()[0] += 1

        # Re-sort populations per ballot box

        cities.sink()
        info[1] -= 1

    print(cities.min()[1])
    sys.stdin.readline()
    info = sys.stdin.readline().split()

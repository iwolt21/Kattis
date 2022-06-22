import sys

class Heap:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.Heap = [["", 0]] * (self.maxSize + 1)

    def insert(self, node):
        self.size += 1
        self.Heap[self.size] = node
        self.swim(self.size)

    def remove(self):
        temp = self.Heap[1]
        self.Heap[1] = self.Heap[self.size]
        self.Heap[self.size] = ["", 0]
        self.size -= 1
        self.sink()
        return temp

    def swim(self, k):
        temp = self.Heap[k]
        while k > 1 and self.Heap[k // 2][0] > temp[0]:
            self.Heap[k] = self.Heap[k // 2]
            k = k // 2
        self.Heap[k] = temp

    def sink(self):
        k = 1
        temp = self.Heap[k]
        while 2 * k <= self.size:
            j = 2 * k
            if j < self.size and self.Heap[j][0] > self.Heap[j + 1][0]:
                j += 1
            if not temp[0] > self.Heap[j][0]:
                break
            self.Heap[k] = self.Heap[j]
            k = j
        self.Heap[k] = temp

    def min(self):
        return self.Heap[1]


info = sys.stdin.readline().split()
info = [int(num) for num in info]
books = Heap(info[0] + info[1] + 1)
count = 0

books.insert(["Jane Eyre", info[2]])

for num in range(info[0]):
    owned = sys.stdin.readline().split("\"")
    books.insert(owned[1:])

received = []

for i in range(info[1]):
    new_book = sys.stdin.readline().split("\"")
    if new_book[1] < "Jane Eyre":
        received.append(new_book)

received.sort(key=lambda x: int(x[0]))
received_book_num = 0
current_book = None
while current_book is None or current_book[0] != "Jane Eyre":
    current_book = books.remove()
    count += int(current_book[1])
    if received_book_num < len(received) and count >= int(received[received_book_num][0]):
        books.insert(received[received_book_num][1:])
        received_book_num += 1

print(count)


class max_heap_sort:
    def __init__(self, arr):
        self.arr = arr

    def leftChild(self, i):
        return 2 * i

    def rightChild(self, i):
        return 2 * i + 1

    def max_heapify(self, end, i):
        l = self.leftChild(i)
        r = self.rightChild(i)
        max = i
        if (l < end and self.arr[i] < self.arr[l]):
            max = l

        elif (r < end and self.arr[max] < self.arr[r]):
            max = r

        if max != i:
            self.swap(i, max)
            self.max_heapify(end, max)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def heap_sort(self):
        end = len(self.arr)
        start = end // 2
        for i in range(end, -1, -1):
            self.max_heapify(end, i)
        return self.arr


class min_heap_sort:
    def __init__(self, arr):
        self.arr = arr

    def leftChild(self, i):
        return 2 * i

    def rightChild(self, i):
        return 2 * i + 1

    def min_heapify(self, end, i):
        l = self.leftChild(i)
        r = self.rightChild(i)
        min = i
        if (l < end and self.arr[i] > self.arr[l]):
            min = l

        elif (r < end and self.arr[min] > self.arr[r]):
            min = r

        if min != i:
            self.swap(i, min)
            self.min_heapify(end, min)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def heap_sort(self):
        end = len(self.arr)
        start = end // 2
        for i in range(end, -1, -1):
            self.min_heapify(end, i)
        return self.arr

arr = [2, 7, 1, -2, 56, 5, 3]

a = max_heap_sort(arr)
print(a.heap_sort())

b = min_heap_sort(arr)
print(b.heap_sort())
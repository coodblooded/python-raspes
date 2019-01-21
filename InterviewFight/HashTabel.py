class Hash:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, query):
        value = query
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            tem = self.tail
            tem.next = new
            tem.previous = tem
            self.tail = new

    def addKey(self, key):
        add_node = Node(0)
        tem_head = self.head
        add_node.next = tem_head
        self.head = add_node

    def addValue(self, value):
        head = self.head
        while head:
            if head.value > 0:
                head.value = head.value + value

            head = head.next


    def get(self, value):

        c = 0
        head = self.head
        while head:
            if head.value == value:
                break
            head = head.next
            c += 1
        return c


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    @property
    def get_value(self):
        return self.value


t = Hash()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.addKey(1)
t.insert(10)
t.insert(15)
t.addKey(1)
print(t.get(10))
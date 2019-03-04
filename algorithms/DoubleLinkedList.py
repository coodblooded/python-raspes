class Node:
    def __init__(self,k):
        self.k = k
        self.next = None
        self.pri = None
        
        
class dubble:
    def __init__(self):
        self.root  = None
        
    def insert(self, k):
        new = Node(k)
        if self.root is None:
            self.root = new
            
        else:
            tem = self.root
            prv = None
            while tem:
                prv = tem
                tem = tem.next
            prv.next = new
            new.pri = prv
            self.root.pri = new
            
            
a = dubble()
a.insert(5)
a.insert(10)
a.insert(15)
a.insert(20)

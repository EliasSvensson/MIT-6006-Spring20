class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        node = Doubly_Linked_List_Node(x)
        if (self.head == None):
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_last(self, x):
        node = Doubly_Linked_List_Node(x)
        if (self.tail == None):
            self.head = node
            self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def delete_first(self):
        x = None
        if (self.head == None):
            return x
        x = self.head.item
        self.head = self.head.next
        if (self.head != None):
            self.head.prev = None
        else:
            self.tail = None
        return x

    def delete_last(self):
        x = None
        if (self.tail == None):
            return x
        x = self.tail.item
        self.tail = self.tail.prev
        if (self.tail != None):
            self.tail.next = None
        else:
            self.head = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        leftNode = x1.prev
        rightNode = x2.next
        L2.head = x1
        L2.tail = x2
        L2.head.prev = None
        L2.tail.next = None

        if (leftNode != None):
            leftNode.next = rightNode
        else:
            self.head = rightNode

        if (rightNode != None):
            rightNode.prev = leftNode
        else:
            L2.tail = leftNode

        return L2

    def splice(self, x, L2):
        if (L2.head == None):
            return L2

        L2.head.prev = x
        L2.tail.next = x.next
        if (x.next != None):
            x.next.prev = L2.tail
        else:
            self.tail = L2.tail

        x.next = L2.head
        L2.head = None
        L2.tail = None
        return L2

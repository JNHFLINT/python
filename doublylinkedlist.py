class Node:
    def __init__(self, val, tail = None, next = None, prev = None):
        self.val = val
        self.tail = tail
        self.next = next
        self.prev = prev

    def __str__(self):
        print(self.val)

    def traverse_forwards(Head):
        curr = Head
        elements = []
        while curr:
            elements.append(curr.val)
            curr = curr.next
        print(elements)

    def traverse_backwards(Head, Tail):
        curr = Tail
        elements = []
        while curr:
            elements.append(curr.val)
            curr = curr.prev
        print(elements)

    def find_element(Head, Target):
        curr = Head
        while curr:
            if curr.val == Target:
                return True
            curr = curr.next
        return False
    
    @staticmethod
    def insert_element(Head, val):
        new_node = Node(val)
        new_node.next = Head
        if Head:
            Head.prev = new_node
        return new_node


Head = Node(5)
Node2 = Node(3)
Node3 = Node(1)
Tail = Node(2)

Head.next = Node2
Node2.prev = Head
Node2.next = Node3
Node3.prev = Node2
Node3.next = Tail
Tail.prev = Node3

Node.__str__(Head)
Node.__str__(Node2)
Node.__str__(Node3)
Node.traverse_forwards(Head)
Node.traverse_backwards(Head, Tail)
print(Node.find_element(Head, 2))
Head = Node.insert_element(Head, 9)
Node.traverse_forwards(Head)
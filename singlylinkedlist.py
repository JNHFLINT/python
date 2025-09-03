# Singly Linked List Implementation

class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        print(self.val)

    # Display linked list in easy to read format
    def display_list(head):
        curr = head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(elements))

    def search_for_element(head, target):
        curr = head
        while curr:
            if curr.val == target:
                return True
            curr = curr.next
        return False
                

# Nodes
Head = SinglyNode(1)
Node1 = SinglyNode(5)
Node2 = SinglyNode(3)

# Pointers
Head.next = Node1
Node1.next = Node2


# Functions
Head.__str__()
Node1.__str__()

SinglyNode.display_list(Head)

print(SinglyNode.search_for_element(Head, 3))
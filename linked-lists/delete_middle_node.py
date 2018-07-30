
class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    '''Linked List using head and tail'''

    def __init__(self):
        self.head = None
        self.tail = None

    def list_print(self):
        node = self.head
        while node:
            print node.data
            node = node.next

    def add_node(self, data):
        '''Add node with data to end of list.'''

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node
        return new_node


def delete_middle_node(node):
    if not node.next:
        raise ValueError('Cannot remove tail node')
    node.data = node.next.data
    node.next = node.next.next


ll = LinkedList()
ll.add_node(300)
ll.add_node(20)
middle_node = ll.add_node(50)
ll.add_node(10)
ll.add_node(15)
delete_middle_node(middle_node)
ll.list_print()



class Node(object):
    """Class in a linked lst."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linkedlst(object):
    '''Linked lst using head and tail'''

    def __init__(self):
        self.head = None
        self.tail = None

    def lst_print(self):
        node = self.head
        while node:
            print node.data
            node = node.next

    def add_node(self, data):
        '''Add node with data to end of lst.'''

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node
        return new_node

def is_intersection(ll1, ll2):

    current = ll1.head = ll2.head

    while current:
        if ll1.head.data == ll2.head.data:
            return True
        current = current.next


    return False


ll1 = Linkedlst()
ll1.add_node(20)
ll1.add_node(10)
ll1.add_node(5)
ll1.add_node(100)
ll1.add_node(10)
ll1.add_node(20)
ll1.add_node(100)

ll2 = Linkedlst()
ll2.add_node(1)
ll2.add_node(2)
ll2.add_node(3)
ll2.add_node(7)
ll2.add_node(4)
ll2.add_node(19)
ll2.add_node(99)

print is_intersection(ll1, ll2)
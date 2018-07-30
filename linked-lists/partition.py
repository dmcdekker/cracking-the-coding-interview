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


def partition (ll, part):
    '''All nodes less than partition come before and those greater come after''' 
    
    # assign head and tail to variable current (first value in LL)
    current = ll.tail = ll.head

    # iterate over nodes 
    while current:
        next_node = current.next
        current.next = None
        # if current is less than part move head to next node
        # reassign head to current
        if current.data < part:
            current.next = ll.head
            ll.head = current
        else:
            # else move current to end (tail)
            # reassign tail to current
            ll.tail.next = current
            ll.tail = current
        # assign next value to current 
        current = next_node
        
    # In case all nodes are less than part value
    if not ll.tail.next:
        ll.tail.next = None

ll = LinkedList()
ll.add_node(50)
ll.add_node(50)
ll.add_node(32)
ll.add_node(26)
ll.add_node(300)
ll.add_node(200)
ll.add_node(-3)
ll.add_node(69)
partition(ll, ll.head.data)
ll.list_print()


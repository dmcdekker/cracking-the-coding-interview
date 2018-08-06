class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node {data}>".format(data=self.data)


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None


    def list_print(self):
        node = self.head
        while node:
            print node.data
            node = node.next

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

def return_kth_to_last(ll, k):
    # set current and variable length
    current = ll.head
    length = 0
    # iterate through list to get length (add 1 to variable length)
    while current:
        length += 1
        current = current.next
    # define number of steps to be taken from head
    steps = length - k
    current = ll.head
    # iterate through list to find correct element
    for i in range(steps):
        print i
        # current = current.next
        
    return current.data


#----with buffer-----
ll = LinkedList()
ll.add_node(100)
ll.add_node(20)
ll.add_node(10)
ll.add_node(50)
ll.add_node(40)
ll.add_node(60)
print return_kth_to_last(ll, 2)
print return_kth_to_last(ll, 4)
print return_kth_to_last(ll, 1)


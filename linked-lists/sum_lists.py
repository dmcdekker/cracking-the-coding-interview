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

def sum_lists(ll1, ll2):
    # get vals of heads
    l1, l2 = ll1.head, ll2.head
    # create LL to hold new values
    ll_sum = LinkedList()
    # variable to hold carry over of summing values
    carry = 0
    while l1 or l2:
        # variable total will always hold value of carry to begin
        total = carry
        # add value of l1 node to total
        if l1:
            total += l1.data
            l1 = l1.next
        # add value of l2 node to total
        if l2:
            total += l2.data
            l2 = l2.next

        # add total sum mod 10 to ll_sum
        ll_sum.add_node(total % 10)
        # carry will be added to next addition
        carry = total // 10

    new_ll = ll_sum.list_print()

    return new_ll

ll1 = LinkedList()
ll2 = LinkedList()
ll1.add_node(7)
ll1.add_node(1)
ll1.add_node(6)
ll2.add_node(5)
ll2.add_node(9)
ll2.add_node(2)
print sum_lists(ll1, ll2)



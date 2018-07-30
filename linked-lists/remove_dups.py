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


def remove_dups(ll):
    # check if linked list exists
    if not ll.head:
        return
    # current is head
    current = ll.head
    # set for easy lookup
    seen = set([current.data])
    # iterate through list; if already seen (dupe)
    # make pointers point to next.next elem 
    # otherwise add to set if not dupe
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

    return ll

# use auxilliary pointer to travel behind the linked list pointer
def remove_dups_followup(ll):
    if not ll.head:
        return
    current = ll.head
    while current:
        aux = current
        while aux.next:
            if aux.next.data == current.data:
                aux.next = aux.next.next
            else:
                aux = aux.next
        current = current.next

    return ll


#----with buffer-----
ll = LinkedList()
ll.add_node(100)
ll.add_node(20)
ll.add_node(10)
ll.add_node(100)
remove_dups(ll)
print '______remove_dups______'
ll.list_print()

#----without buffer-----
ll = LinkedList()
ll.add_node(300)
ll.add_node(20)
ll.add_node(300)
ll.add_node(10)
remove_dups_followup(ll)
print '______remove_dups_followup______'
ll.list_print()
# print(ll)

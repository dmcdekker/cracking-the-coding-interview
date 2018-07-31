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

# solution that uses list reversal to compare
def palindrome(ll):
    current = ll.head
    stack = []
    while current:
        stack.append(current.data)
        current = current.next
    if stack == stack[::-1]:
        return True
    return False

# use stack (my version of CTCI solution)
def is_palindrome(ll):

    stack = []
    current = ll.head

    # add items in LL to the stack
    while current:
        stack.append(current.data)
        current = current.next

    # compare LL node data to stack: popped items will equal 
    # LL items if list is a palindrome
    current = ll.head
    while current:
        if stack.pop() != current.data:
            return False
        current = current.next

    return True

            
#----True Palindrome-----
ll1 = Linkedlst()
ll1.add_node(100)
ll1.add_node(20)
ll1.add_node(10)
ll1.add_node(5)
ll1.add_node(10)
ll1.add_node(20)
ll1.add_node(100)
print '______palindrome (rev lst)______'
print palindrome(ll1)
print '______is_palindrome (stack)______'
print is_palindrome(ll1)

#----False Palindrome-----
ll2 = Linkedlst()
ll2.add_node(100)
ll2.add_node(20)
ll2.add_node(15)
ll2.add_node(7)
ll2.add_node(10)
ll2.add_node(20)
ll2.add_node(100)
print '______palindrome (rev lst)______'
print palindrome(ll2)
print '______is_palindrome (stack)______'
print is_palindrome(ll2)

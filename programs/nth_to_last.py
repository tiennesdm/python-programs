class Node:
    def __init__(self,value):
        self.value=value
        self.nextnode=None
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=e
def nth_to_last(n,head):
    left_pointer=head
    right_pointer=head
    for i in xrange(n-1):
        if not right_pointer.nextnode:
            raise LookupError('Error : n is larger ')
        right_pointer=right_pointer.nextnode
    while right_pointer.nextnode:
        left_pointer=left_pointer.nextnode
        right_pointer=right_pointer.nextnode
    return left_pointer
target_node=nth_to_last(2,a)
print target_node.value

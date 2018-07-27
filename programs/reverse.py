class Node:
    def __init__(self,value):
        self.value=value
        self.nextnode=None
def reverse(head):
    curent=head
    previous=None
    nextnode=None
    while curent:
        nextnode=curent.nextnode
        curent.nextnode=previous
        previous=curent
        curent=nextnode
    return previous

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=e
print a.nextnode.value
print b.nextnode.value
print c.nextnode.value
print reverse(a)
print d.nextnode.value
print c.nextnode.value
print b.nextnode.value

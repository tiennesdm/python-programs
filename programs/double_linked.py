class doublelinkedlist(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        self.prevnode=None
a=doublelinkedlist(1)
b=doublelinkedlist(2)
c=doublelinkedlist(3)
a.prevnode=c
a.nextnode=b
b.prevnode=a
b.nextnode=c

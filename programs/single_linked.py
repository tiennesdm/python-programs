class singlelinkedlist(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None
a=singlelinkedlist(1)
b=singlelinkedlist(2)
c=singlelinkedlist(2)
a.nextnode=b
b.nextnode=c



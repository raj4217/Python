class Node(object):

    def __init__(self, value):

        self.value = value
        self.nextnode = None


def reverse(prev, cur):
    if cur:
        reverse(cur, cur.nextnode)
        cur.nextnode = prev



# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

reverse(a)

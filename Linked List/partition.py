# not working


from node_file import Node

def do_partition(node, number):
    head = node
    tail = node
    while node is not None:
        next = node.next
        if node.data < number:
            node.next = head
            head = node
        else:
            tail.next = node



def main():
    n1 = Node(11)
    n2 = Node(5)
    n3 = Node(2)
    n4 = Node(8)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    do_partition(n1,5)



main()

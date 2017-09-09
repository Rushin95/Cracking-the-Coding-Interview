# delete a node from middle just using that node

from node_file import Node

def del_mid_node(input_node):
    current_node = input_node
    while current_node.next is not None:
        current_node.data = current_node.next.data
        print current_node.next.data, 'moved to previous node'
        previous_node = current_node
        current_node = current_node.next
        print current_node.data, ' is now the current node'
    previous_node.next = None
    print 'node deleted'

    # try short method

def main():
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    del_mid_node(n2)
    n1.printNodes()


main()

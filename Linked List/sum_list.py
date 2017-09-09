# try it again


from node_file import Node

def do_sum(node_1, node_2):
    a_node = node_1
    b_node = node_2
    ans = []
    data_sum = 0
    idx = 1
    new


    while a_node is not None and b_node is not None:
        data_sum += (a_node.data*idx) + (b_node.data*idx)
        ans.append(data_sum/(idx))


        new = Node(data_sum/(idx))


        new.data = data_sum/idx
        new.next = Node(None)
        new = new.next
        idx *= 10
        a_node, b_node = a_node.next, b_node.next

    head.printNodes()
    print ans

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    m1 = Node(1)
    m2 = Node(2)
    m3 = Node(3)
    m4 = Node(4)
    m1.next = m2
    m2.next = m3
    m3.next = m4


    do_sum(n1,m1)

main()

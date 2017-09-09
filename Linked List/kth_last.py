# determine the kth element of the linked list from the end

from node_file import Node

def find_kth_last(head,k):
    if head is None or k < 1:
        return 0

    current_node = head
    idx = 1
    while current_node.next is not None:
        idx += 1
        current_node = current_node.next
    current_node = head

    for _ in xrange(idx - k):
        current_node = current_node.next
    return current_node.data

def find_kth_last_recursive(head,k):
    if head is None or k < 1:
        return 0
    idx = find_kth_last_recursive(head.next,k) + 1
    if idx == k:
        print head.data
    return idx

def main():
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    print find_kth_last(n1,3)
    find_kth_last_recursive(n1,3)

main()

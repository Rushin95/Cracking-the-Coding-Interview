
from node_file import Node

def is_palidrome(head):
    previous_node = head
    current_node - previous_node.next
    next_node = current_node.next

    while next_node is not None:
        previous_node.next = next_node
        current_node.next = previous_nodemeam

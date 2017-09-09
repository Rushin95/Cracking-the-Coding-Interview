# remove any nodes with duplicate values from the linked list

from node_file import Node

def remove_dup(input_node):
    previous_node = input_node
    parsed = []
    parsed.append(previous_node.data)
    current_node = previous_node.next
    while current_node is not None:
            if current_node.data not in parsed:
                parsed.append(current_node.data)
                previous_node = current_node
                current_node = current_node.next
            else:
                previous_node.next = current_node.next
                current_node.next = None
                current_node = previous_node.next
    return parsed
def main():
    n1 = Node(10)
    n2 = Node(10)
    n3 = Node(20)
    n4 = Node(10)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    print remove_dup(n1)

main()

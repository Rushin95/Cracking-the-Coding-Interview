class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def getLength(self):
        current_node = self
        idx = 1
        while current_node.next is not None:
            idx += 1
            current_node = current_node.next
        return idx

    def printNodes(self):
        nodes = []
        current_node = self
        while current_node is not None:
            nodes.append(current_node.data)
            current_node = current_node.next
        print 'Linked List: ', nodes

    def getNodes(self):
        nodes = []
        current_node = self
        while current_node is not None:
            nodes.append(current_node.data)
            current_node = current_node.next
        return nodes

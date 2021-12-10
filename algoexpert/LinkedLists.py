class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)  # set data
        new_node.next = self.head  # set next
        self.head = new_node  # update head

    def delete_node(self, key):
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = Node  # free memory
                return

        while temp is not None:
            if temp.data == key:    break
            prev, temp = temp, temp.next  # find previous node(prev) of the node(temp) to be deleted

        if temp is None: return  # no key
        prev.next = temp.next  # change the next of previous node
        temp = None  # free memory

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.head, second, third = Node(1), Node(2), Node(3)
    llist.head.next, second.next = second, third
    llist.printList()

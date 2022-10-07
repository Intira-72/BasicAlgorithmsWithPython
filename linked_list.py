class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def traversal(self):
        first = self.head

        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_node):
        new_node = Node(new_node)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head

        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

    def delete_node(self, x):
        temp = self.head

        while temp is not None:
            if temp.data == x:
                break
            perv = temp
            temp = temp.next
        perv.next = temp.next

    def delete_tail(self):
        temp = self.head

        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


if __name__ == "__main__":
    family = LinkedList()
    family.head = Node("Bob")
    wife = Node("Amy")
    first_kid = Node("Max")
    second_kid = Node("Jenny")

    family.head.next = wife
    wife.next = first_kid
    first_kid.next = second_kid

    family.insert_new_header("Dave")
    # print(family.search("Bob"))
    family.delete_node("Bob")
    family.delete_tail()

    family.traversal()
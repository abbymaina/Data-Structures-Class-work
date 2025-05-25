# class linkedListNode:
#     def __init__(self, value, nextNode = None):
#         self.value = value
#         self.nextNode = nextNode

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next =None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#



    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data)

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')

            temp = temp.next
        print()

if __name__ == '__main__':
    llist = LinkedList()

    llist.insertAtTheBeginning("Fox")
    llist.insertAtTheBeginning("Brown")
    llist.insertAtTheBeginning("Quick")
    llist.insertAtTheBeginning("The")

    llist.printLinkedList()

    llist.insertAtTheEnd()




class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # prints all values of every node in the linked list
    def printAllVals(self):
        runner = self.head
        while (runner.next != None):
            print(runner.val)
            runner = runner.next
        print runner.val

    # adds node with a given value to the end of the linked list
    def addBack(self, val):
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = Node(val)

    # adds node with a given value to the front of the linked list
    def addFront(self, val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp

    # adds node with a given value before the given reference value
    def insertBefore(self, nextVal, val):
        # handles cases where the reference value is the head of the linked list
        if (self.head.val == nextVal):
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
        # handles other cases where the reference value is not the head of the linked list
        else:
            runner = self.head
            while (runner.next.val != nextVal):
                runner = runner.next
            temp = runner.next
            runner.next = Node(val)
            runner.next.next = temp

    # adds node with a given value after the given reference value
    def insertAfter(self, preVal, val):
        # handles cases where the reference value is the head of the linked list
        if (self.head.val == preVal):
            temp = self.head.next
            self.head.next = Node(val)
            self.head.next.next = temp
        # handles other cases where the reference value is not the head of the linked list
        else:
            runner = self.head
            while (runner.next.val != preVal):
                runner = runner.next
            if (runner.next.val == preVal):
                runner = runner.next
            temp = runner.next
            runner.next = Node(val)
            runner.next.next = temp

    # deletes node with the given value
    def removeNode(self, val):
        # handles cases where the node we want to remove is the head of the linked list
        if (self.head.val == val):
            self.head = self.head.next
        # handles other cases where the node we want to remove is not the head of the linked list
        else:
            runner = self.head
            while (runner.next.val != val):
                runner = runner.next
            runner.next = runner.next.next

    # reverses the contents of the linked list
    def reverseList(self):
        runner = self.head
        nextNode = None
        prevNode = None
        while (runner != None):
            nextNode = runner.next
            runner.next = prevNode
            prevNode = runner
            runner = nextNode
        self.head = prevNode

list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')

list.addBack('Tom')
list.addFront('Aaron')
list.insertBefore('Debra', 'Erika')
list.insertAfter('Tom', 'Will')
list.removeNode('Debra')
list.reverseList()
list.printAllVals()

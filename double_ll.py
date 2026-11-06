class Node:
    pass


class DoublyList:
    def initialize(self):
        self.head = None
        self.tail = None

    def pushFront(self, value):
        newNode = Node()
        newNode.data = value
        newNode.next = None
        newNode.prev = None

        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def pushBack(self, value):
        newNode = Node()
        newNode.data = value
        newNode.next = None
        newNode.prev = None

        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def popFront(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
            return

        temp = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

        temp.next = None

    def popBack(self):
        if self.tail is None:
            print("Doubly Linked List is Empty")
            return

        temp = self.tail
        self.tail = self.tail.prev

        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

        temp.prev = None

    def printList(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


dll = DoublyList()
dll.initialize()

while True:
    print("\n1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Delete from End")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        dll.pushFront(value)

    elif choice == 2:
        value = int(input("Enter value: "))
        dll.pushBack(value)

    elif choice == 3:
        dll.popFront()

    elif choice == 4:
        dll.popBack()

    elif choice == 5:
        dll.printList()

    elif choice == 6:
        break

    else:
        print("Invalid Choice")

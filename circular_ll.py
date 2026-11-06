class Node:
    pass


class CircularList:

    def initialize(self):
        self.head = None
        self.tail = None

    def insertAtHead(self, value):
        newNode = Node()
        newNode.data = value
        newNode.next = None

        if self.head is None:
            self.head = self.tail = newNode
            self.tail.next = self.head
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head

    def insertAtTail(self, value):
        newNode = Node()
        newNode.data = value
        newNode.next = None

        if self.head is None:
            self.head = self.tail = newNode
            self.tail.next = self.head
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode

    def deleteAtHead(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            temp.next = None

    def deleteAtTail(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head

            while temp.next != self.tail:
                temp = temp.next

            self.tail = temp
            self.tail.next = self.head

    def printList(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(head:", self.head.data, ")")


cll = CircularList()
cll.initialize()

while True:
    print("\n1. Insert at Head")
    print("2. Insert at Tail")
    print("3. Delete at Head")
    print("4. Delete at Tail")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        cll.insertAtHead(value)

    elif choice == 2:
        value = int(input("Enter value: "))
        cll.insertAtTail(value)

    elif choice == 3:
        cll.deleteAtHead()

    elif choice == 4:
        cll.deleteAtTail()

    elif choice == 5:
        cll.printList()

    elif choice == 6:
        break

    else:
        print("Invalid choice")

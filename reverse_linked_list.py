def create():
    head = None
    curr = None

    n = int(input("Enter Number of Nodes: "))
    val = list(map(int, input("Enter values: ").split()))

    for i in range(n):
        newnode = {"val": val[i], "next": None}

        if head is None:
            head = newnode
            curr = newnode
        else:
            curr["next"] = newnode
            curr = newnode

    return head

def reverse(head):
    prev = None
    curr = head
    while curr is not None:
        nxt = curr["next"]
        curr["next"] = prev
        prev = curr
        curr = nxt
    return prev


def printlist(head):
    curr = head

    while curr is not None:
        print(curr["val"], end=" -> ")
        curr = curr["next"]

    print("None")


head = create()

print(" Orignal Linked List : ")
printlist(head)
head = reverse(head)
print("Reverse Linked List : ")
printlist(head)

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

def middle(head):
    slow = head
    fast = head

    while (fast is not None) and (fast["next"] is not None):
        slow = slow["next"]
        fast = fast["next"]["next"]

    return slow

def printlist(head):
    curr = head

    while curr is not None:
        print(curr["val"], end=" -> ")
        curr = curr["next"]

    print("None")


head = create()
print("Linked List:")
printlist(head)

mid = middle(head)

if mid is not None:
    print("Middle Element of Linked List is:", mid["val"])
else:
    print("Linked List is Empty")
    
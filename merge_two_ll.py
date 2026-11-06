class ListNode:
    pass

def create():
    n = int(input("Enter number of nodes: "))
    values = list(map(int, input("Enter values: ").split()))

    head = None
    curr = None

    for i in range(n):
        newnode = ListNode()
        newnode.val = values[i]
        newnode.next = None

        if head is None:
            head = curr = newnode
        else:
            curr.next = newnode
            curr = newnode

    return head


def merge(h1, h2):
    if h1 == None:
        return h2

    if h2 == None:
        return h1

    if h1.val <= h2.val:
        h1.next = merge(h1.next, h2)
        return h1
    else:
        h2.next = merge(h1, h2.next)
        return h2


def display(head):
    curr = head

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


print("First Sorted Linked List:")
h1 = create()

print("\nSecond Sorted Linked List:")
h2 = create()

print("\nMerged Linked List:")
head = merge(h1, h2)

display(head)
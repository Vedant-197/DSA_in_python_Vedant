class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        m = {}

        oldTemp = head

        while oldTemp is not None:
            copyNode = Node(oldTemp.val)
            m[oldTemp] = copyNode
            oldTemp = oldTemp.next

        oldTemp = head

        while oldTemp is not None:
            copyNode = m[oldTemp]

            if oldTemp.next is not None:
                copyNode.next = m[oldTemp.next]

            if oldTemp.random is not None:
                copyNode.random = m[oldTemp.random]

            oldTemp = oldTemp.next

        return m[head]


def createList():
    n = int(input("Enter number of nodes: "))

    if n == 0:
        return None

    nodes = []

    for i in range(n):
        val = int(input(f"Enter value of node {i}: "))
        nodes.append(Node(val))

    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]

    print("\nEnter random pointer indices (-1 for None):")

    for i in range(n):
        r = int(input(f"Random index for node {i}: "))

        if r != -1:
            if 0 <= r < n:
                nodes[i].random = nodes[r]
            else:
                print("Invalid index. Random pointer set to None.")

    return nodes[0]


def display(head):
    temp = head
    index = 0

    while temp is not None:
        randomValue = temp.random.val if temp.random else None
        print(f"Node {index}: Value = {temp.val}, Random = {randomValue}")
        temp = temp.next
        index += 1


head = createList()

obj = Solution()
copyHead = obj.copyRandomList(head)

print("\nOriginal Linked List:")
display(head)

print("\nCopied Linked List:")
display(copyHead)
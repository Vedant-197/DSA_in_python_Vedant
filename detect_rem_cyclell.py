class Solution:

    def hascycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def detect_cycle(self, head):
        slow = head
        fast = head
        iscycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                iscycle = True
                break

        if not iscycle:
            return None

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    def removeCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return

        slow = head

        if slow == fast:
            while fast.next != slow:
                fast = fast.next

            fast.next = None
            return

        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = None


class ListNode:
    pass


def create():
    n = int(input("Enter number of nodes: "))
    values = list(map(int, input("Enter values: ").split()))

    head = None
    curr = None
    nodes = []

    for i in range(n):
        newnode = ListNode()
        newnode.val = values[i]
        newnode.next = None

        nodes.append(newnode)

        if head is None:
            head = curr = newnode
        else:
            curr.next = newnode
            curr = newnode

    pos = int(input("Enter cycle position (0 for no cycle): "))

    if pos > 0 and pos <= n:
        curr.next = nodes[pos - 1]

    return head


def display(head):
    curr = head

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


obj = Solution()

head = create()

print("\nCycle Detection:")
print(obj.hascycle(head))

print("\nCycle Starting Node:")
start = obj.detect_cycle(head)

if start:
    print(start.val)
else:
    print("No cycle")

print("\nRemoving Cycle:")
obj.removeCycle(head)

display(head)
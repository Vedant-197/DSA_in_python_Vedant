q = list(map(int, input("Enter queue elements: ").split()))

print("Queue:", q)

# Enqueue
x = int(input("Enter element to enqueue: "))
q.append(x)
print("After Enqueue:", q)

# Dequeue
if len(q) > 0:
    print("Dequeued element:", q.pop(0))
else:
    print("Queue is empty")

print("Queue after Dequeue:", q)

# Front
if len(q) > 0:
    print("Front element:", q[0])

# Rear
if len(q) > 0:
    print("Rear element:", q[-1])

# Size
print("Queue size:", len(q))

# IsEmpty
print("Is Queue Empty:", len(q) == 0)
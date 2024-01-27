from collections import deque

customQueue = deque(maxlen=3)

print(customQueue)

# append = enqueue
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)

print(customQueue)

customQueue.append(4)
print(customQueue)

# popleft = dequeue

print(customQueue.popleft())

# delete = clear
customQueue.clear()

print(customQueue)
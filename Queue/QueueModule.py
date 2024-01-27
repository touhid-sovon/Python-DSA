import queue as q

customQueue = q.Queue(maxsize=3)

# qsize = len()
print(customQueue.qsize())

# empty
print(customQueue.empty())

# put = enqueue
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)

#full
print(customQueue.full())

# get = dequeue
print(customQueue.get())
print(customQueue.get())

print(customQueue.task_done())

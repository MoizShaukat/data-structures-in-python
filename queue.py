from queue import Queue

q = Queue(maxsize=5)

for i in range(15, 20):
    q.put(i)

print('queue is full: ', q.full())

print(list(q.queue))

for j in range(15, 20):
    print(q.get(j), 'is popped')

print('queue is empty: ', q.empty())

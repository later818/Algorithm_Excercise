from collections import deque

q = deque()
q.append([11, 22])
print(q[0][0])
x, y = q.popleft()
print(x, y)

c = [11, 22]
print(type(c))
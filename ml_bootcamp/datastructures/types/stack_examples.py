from collections import deque
from queue import LifoQueue
stack = ['a', 'b', 'c']
print('Initial stack', stack)
stack = deque()
stack.append('d')
stack.append('e')
stack.append('f')
print('After append', stack)
stack.pop()
print('After pop', stack)
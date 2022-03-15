from inspect import isfunction
import sys


class MyCircularQueue:
  
    def __init__(self, k: int):
        self.queue = [None] * k
        self.size = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.rear] = value
            self.rear += 1
            if self.rear == self.size:
                self.rear = 0
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.front] = None
            self.front += 1
            if self.front == self.size:
                self.front = 0
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear -1]

    def isEmpty(self) -> bool:
        if self.front == self.rear and self.queue[self.front] is None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.front == self.rear and self.queue[self.rear] is not None:
            return True
        else:
            return False
    
# # Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print('obj = MyCircularQueue(3)', '\nqueue: ' + str(obj.queue), '\nfront ' + str(obj.front), 'rear: '+ str(obj.rear), '\n')
param_1 = obj.enQueue(1)
print('enQueue(1)', '\nqueue: ' + str(obj.queue), '\nfront ' + str(obj.front), 'rear: '+ str(obj.rear), '\n')
param_2 = obj.enQueue(2)
print('enQueue(2)', '\nqueue: ' + str(obj.queue), '\nfront ' + str(obj.front), 'rear: '+ str(obj.rear), '\n')
param_3 = obj.enQueue(3)
print('enQueue(3)', '\nqueue: ' + str(obj.queue), '\nfront ' + str(obj.front), 'rear: '+ str(obj.rear), '\n')
param_4 = obj.enQueue(4)
print('enQueue(4)', '\nqueue: ' + str(obj.queue), '\nfront ' + str(obj.front), 'rear: '+ str(obj.rear), '\n')
param_5 = obj.Rear()
print('Rear()', '\nqueue: ' + str(obj.queue), '\nfront ' + str(obj.front), 'rear: '+ str(obj.rear))
print('Rear()', 'result: ' + str(param_5), '\n')
param_6 = obj.isFull()
print('isFull()', '\nqueue: ' + str(obj.queue), '\nfront ' + str(obj.front), 'rear: '+ str(obj.rear))
print('isFull()', 'result: ' + str(param_6), '\n')
param_7 = obj.deQueue()
print('deQueue()', '\nqueue: ' + str(obj.queue), '\nfront ' + str(obj.front), 'rear: '+ str(obj.rear), '\n')
param_8 = obj.enQueue(4)
print('enQueue(4)', '\nqueue: ' + str(obj.queue), '\nfront ' + str(obj.front), 'rear: '+ str(obj.rear), '\n')
param_9 = obj.Rear()
print('Rear()', '\nqueue: ' + str(obj.queue), '\nfront ' + str(obj.front), 'rear: '+ str(obj.rear))
print('Rear()', 'result: ' + str(param_9), '\n')


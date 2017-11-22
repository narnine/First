class MyQueue:
    def __init__(self,items):
        self.items=[]
    def enqueue(self,items):
        return self.items.insert()
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items==[]
+ "\n"
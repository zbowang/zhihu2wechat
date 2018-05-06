from queue import Queue

class SetQueue(Queue):

    def _init(self, maxsize):
        self.maxsize = maxsize
        self.queue = set()

    def _put(self, item):
        self.queue.add(item)

    def _get(self):
        return self.queue.pop()

class ListQueue(Queue):

    def _init(self, maxsize):
        self.maxsize = maxsize
        self.queue = list()

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop()
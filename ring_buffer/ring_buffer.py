class RingBuffer:
    def __init__(self, capacity):
        # assign values with buffer being our empty list and old being 0 to reference the first item in our list
        self.capacity = capacity
        self.buffer = []
        self.old = 0

    def append(self, item):
        # check if our empty list is less than our capacity
        if len(self.buffer) < self.capacity:
            # if it is then our buffer needs to be appended by our item until the if statement is false
            self.buffer.append(item)
        else:
            # remove our oldest value from the buffer list
            self.buffer.remove(self.buffer[self.old])
            # insert our now oldest reference into the item part of the list or our newest element
            self.buffer.insert(self.old, item)
            # add old + 1 to move through the capacity of the list to repeat the process
            if self.old + 1 < self.capacity:
                self.old += 1
            # reset the oldest element in the list back to the first one coming in which was 0
            else:
                self.old = 0

    def get(self):
        # simply return the buffer list to see our value
        return self.buffer

import ctypes
class DynamicArray(object):
    # constructor
    def __init__(self):
        self.n = 0
        self.capacity = 1
        # create initial array of size 1
        self.A = self.make_array(self.capacity)

    # get array length
    def __len__(self):
        return self.n

    # get item from array
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('Index K is out of bounds')

        return self.A[k]

    # append an item to array
    def append(self, element):
        if self.n == self.capacity:
            self._resize(2 * self.capacity) # double size if at capacity
        
        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):
        # create new array larger capacity
        B = self.make_array(new_capacity)

        # copy over elements from existing array
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity

    # make a new array using ctypes
    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

# Test it out...
arr = DynamicArray()
arr.append(1)
print len(arr)
arr.append(2)
print len(arr)
print arr[0]
print arr[1]
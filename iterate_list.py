class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

# Example usage
numbers = [10, 20, 30, 40, 50]
custom_iter = CustomIterator(numbers)

while True:
    try:
        print(next(custom_iter))
    except StopIteration:
        break



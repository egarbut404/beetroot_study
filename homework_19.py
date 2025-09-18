### Task 1 ###

def with_index(iterable, start=0):
    n = start
    for item in iterable:
        yield n, item
        n += 1

my_list = ['a', 'b', 'c']

for index, value in with_index(my_list):
    print(index, value)

### Task 2 ###

def in_range(start, end, step = 1):

    if step == 0:
        raise ValueError("The step cannot be equal to zero")

    current = start

    if step > 0:
        while current < end:
            yield current
            current += step
    else:
        while current > end:
            yield current
            current += step

for i in in_range(1, 10, 2):
    print(i)


### Task 3 ###

class CustomList:

    def __init__(self, items: list = None):
        self._items = list(items) if items is not None else []

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def append(self, item):
        self._items.append(item)

custom_list = CustomList(['a','b','c','d','e','f'])

for item in custom_list:
    print(item)

print(custom_list[0])

def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100  # assuming 100 is the size of the list


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, val)
                return

        self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t = HashTable()
t['march 9'] = 120
t['marhc 9'] = 130

print(t['march 9'])
print(t.arr)

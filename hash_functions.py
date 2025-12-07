class HashTable:
    def __init__(self, bucket):
        self.bucket = bucket
        self.table = [[] for _ in range(bucket)]

    def hash(self, key):
        return (key % self._bucket)
    
    def insertItem(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def lookUp(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

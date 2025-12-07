class HashTable:
    def __init__(self, bucket):
        self.__bucket = bucket
        self.__table = [[] for _ in range(bucket)]

    def hash(self, key):
        return (key % self._bucket)
    
    def insertItem(self, key, value):
        index = self.hash(key)
        self.__table[index].append((key, value))

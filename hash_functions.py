class HashTable:
    def __init__(self, bucket):
        self.bucket = bucket
        self.table = [[] for _ in range(bucket)]

    def hash(self, key):
        return (key % self.bucket)
    
    def insertItem(self, object):
        index = self.hash(object.id)
        self.table[index].append((object.id, object))

    def lookUp(self, object):
        index = self.hash(object.id)
        for key, obj in self.table[index]:
            if key == object.id:
                return obj    
        return None
    
    def __str__(self):
        for i, bucket in enumerate(self.table):
            print(f'bucket {i}: {bucket}\n')

    def __repr__(self):
        for i, bucket in enumerate(self.table):
            print(f'bucket {i}: {bucket}\n')

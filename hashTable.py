class HashTable:
    def __init__(self, bucket):
        self.bucket = bucket
        self.table = [[] for _ in range(bucket)]

    def hash(self, key):
        return (int(key) % self.bucket)
    
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
        buckets = ''
        for i, bucket in enumerate(self.table):
            buckets += f'\nbucket {i}:'
            buckets += '\n'
            buckets += '---------------------------------------------------------------------'
            buckets += '\n'
            for item in bucket:
                buckets += f'{item} \n'
        return buckets

    def __repr__(self):
        buckets = ''
        for i, bucket in enumerate(self.table):
            buckets += f'bucket {i}:\n'
            for item in bucket:
                buckets += f'{item}\n\n'
        return buckets

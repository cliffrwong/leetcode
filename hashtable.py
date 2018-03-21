import math

def hashfunc(key_str, size):
    return sum([ord(a) for a in key_str]) % size

class HashTable:

    def __init__(self, capacity=997):
        self.capacity = capacity
        self.size = 0
        self.load_factor = .75
        self._keys = []
        self.hash = [[] for _ in capacity]
        
    def _find_by_key(self, key, find_result_func):
        index = hash_function(key, self.capacity)
        hash_table_cell = self.hash[index]
        found_item = None
        for item in hash_table_cell:
            if item[0] == key:
                found_item = item
        find_result_func(found_item, hash_table_cell)
        
    def get(self, key):
        def find_result_func(found_item, _):
            if found_item is None:
                raise KeyError(key)
            else:
                return found_item[1]
        return self._find_by_key(key, find_result_func)
        
    def set(self, key, value):
        def find_result_func(found_item, hash_table_cell):
            if found_item is None:
                hash_table_cell.append([key, value])
                self.size += 1
                self._keys.append(key)
                if self.size >= self.capacity*self.load_factor:
                    self.rehash()
            else:
                for item in hash_table_cell:
                    if item[0] == key:
                        item[1] = value
                        break
        return self._find_by_key(key, find_result_func)
        
    def upPrime(self, n):
        for num in range(n, 2n ,2):
            if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
                return num
    def rehash(self):
        self.capacity = self.up_prime(2*self.capacity+1)
        self.old_hash = self.hash
        self.hash = [[] for _ in range(self.capacity)]
        for hash_table_cell in self.old_hash:
            for item in hash_table_cell:
                self.set(item[0], item[1])
        
    def remove(self, key):
        def find_result_func(found_item, hash_table_cell):
            if found_item is None:
                raise KeyError(key)
            else:
               hash_table_cell.remove(found_item)
               self._keys.remove(found_item[0])
               self.size -= 1
               return found_item[1]
            
    def keys(self):
        return self._keys
        
    def __setitem__(self, key, value):
        self.set(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
        
    def __delitem__(self, key):
        return self.remove(key)
    
    def __repr__(self):
        return '{' + ', '.join([str(key)+': ' + str(self.get(key)) for key in self._keys]) + ' }'
        
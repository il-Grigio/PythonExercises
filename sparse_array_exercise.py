from multiprocessing.sharedctypes import Value


class SparseArray:
    def __init__(self, array):
        self.lenth = len(array)
        for i, item in enumerate(array):
            if item != 0:
                self.d[i] = (item)
                
    def __len__ (self):
        return self.lenth
    
    def __getitem__(self, index):
        if index >= self.lenth:
            raise IndexError()
        if index in self.data:
            return self.d[index]
        return 0

    def __setitem__(self, index, value):
        if index >= self.lenth:
            raise IndexError()
        
        if value != 0:
            self.d[index] = value
        
        elif index in self.d:
            del self.d[index]
        
    
    def __delitem__(self, index):
        del self._data[index]
        self.d = {k if k < index else k -1: v for k, v in self.d.items()} ##k= key, v = value
        self.lenth -= 1


    def __repr__(self):
        rep = self.d
        return rep
    
    def append(self, value):
        if value != 0:
            self.d[self.lenth] = value
        self.lenth += 1


sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
print(sa)
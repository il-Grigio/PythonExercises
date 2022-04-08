class SparseArray:
    d = {}
    def __init__(self, array):
        i = 0
        for item in array:
            self.d[i].append(item)
            i += 1
    
    def __repr__(self):
        rep = self.d
        return rep


sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
print(sa)
import numpy as np

class DataClass1(object):
    """docstring for A"""
    def __init__(self):
        self.data = np.zeros((60,3,32,32))
        self.indexes =  np.arange(self.data.shape[0])
        print(self.data.shape, self.indexes)

    def __len__(self):
        return self.data.shape[0]

if __name__ == '__main__':
    A = DataClass1()
    print(len(A))
    print(A[0])
from mnist import train_images, test_images, train_labels, test_labels
import numpy as np

class MNIST(object):
    """docstring for A"""
    def __init__(self, mode='train'):
        if mode is 'train':
            self.data, self.labels = train_images(), train_labels()
        elif mode is 'test':
            self.data, self.labels = test_images(), test_labels()
        self.indexes =  np.arange(self.data.shape[0])
        np.random.shuffle(self.indexes)

    def __len__(self):
        return self.data.shape[0]

    def __getitem__(self, indexes):
        return self.data[self.indexes[indexes]]

if __name__ == '__main__':
    train_data = MNIST('train')
    test_data = MNIST('test')
    print(len(train_data), len(test_data))

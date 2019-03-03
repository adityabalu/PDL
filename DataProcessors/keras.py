from mnist import train_images, test_images, train_labels, test_labels
import numpy as np
import keras

class MNIST(keras.utils.Sequence):
    """docstring for A"""
    def __init__(self, mode='train', batch_size=64):
        if mode is 'train':
            self.data, self.labels = train_images(), train_labels()
        elif mode is 'test':
            self.data, self.labels = test_images(), test_labels()
        self.indexes =  np.arange(self.data.shape[0])
        self.n_classes = 10
        np.random.shuffle(self.indexes)
        self.batch_size = batch_size
        if mode = 'train':
            self.shuffle = True
        else:
            self.shuffle = False
        self.on_epoch_end()

    def __len__(self):
        return int(np.floor(self.data.shape[0] / self.batch_size))

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]
        return self.data[self.indexes[indexes]], keras.utils.to_categorical(self.labels[self.indexes[indexes]], num_classes=self.n_classes)

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.data.shape[0]))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

if __name__ == '__main__':
    train_data = MNIST('train')
    test_data = MNIST('test')

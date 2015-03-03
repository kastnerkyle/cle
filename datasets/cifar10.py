import ipdb
import numpy as np
import theano.tensor as T
from cle.cle.data import DesignMatrix


class CIFAR10(DesignMatrix):
    """
    CIFAR10 batch provider

    Parameters
    ----------
    .. todo::
    """
    def __init__(self, **kwargs):
        super(CIFAR10, self).__init__(**kwargs)
        self.data = self.load_data()
        self.ndata = self.num_examples()
        if self.batchsize is None:
            self.batchsize = self.ndata
        self.nbatch = int(np.float(self.ndata / float(self.batchsize)))
        self.index = -1

    def load_data(self):
        X = np.load(self.path[0])
        y = np.load(self.path[1])
        return (X, y)

    def num_examples(self):
        return self.data[0].shape[0]

    def batch(self, data, i):
        batch = data[i*self.batchsize:(i+1)*self.batchsize]
        return batch

    def __iter__(self):
        return self

    def next(self):
        self.index += 1
        if self.index < self.nbatch:
            return (self.batch(data, self.index) for data in self.data)
        else:
            self.index = -1
            raise StopIteration()

    def theano_vars(self):
        return [T.fmatrix('x'), T.fmatrix('y')]
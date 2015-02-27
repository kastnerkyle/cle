import ipdb
import numpy as np


class Data(object):
    """
    Abstract class for data

    Parameters
    ----------
    .. todo::
    """
    def __init__(self):
        raise NotImplementedError(
            str(type(self)) + " does not implement Data.init.")

    def num_examples(self):
        raise NotImplementedError(
            str(type(self)) + " does not implement Data.num_examples.")

    def batch(self, i):
        raise NotImplementedError(
            str(type(self)) + " does not implement Data.batch.")

    def theano_vars(self):
        raise NotImplementedError(
            str(type(self)) + " does not implement Data.theano_vars.")


class DesignMatrix(Data):

# make path and load it inside
# let any dataset class to define
# its own load function and hack it
# this is more user friendly
# the input-output for this class is just
# their path and batch output.
# They can do whatever crazy hacks for loading
# preprocessing

    def __init__(self, name, path, batch_size=None):
        self.path = path

        self.name = name
        self.data = data
        self.ndata = self.num_examples()
        self.batch_size = batch_size if batch_size is not None else self.ndata
        self.nbatch = int(np.ceil(self.ndata / float(self.batch_size)))
        self.index = -1

    def load_data(self):
        np.load()

    def num_examples(self):
        return self.data[0].shape[0]

    def batch(self, data, i):
        size = self.batch_size
        ndata = self.ndata
        return data[i*size:min((i+1)*size, ndata)]

    def __iter__(self):
        return self

    def next(self):
        self.index += 1
        if self.index < self.nbatch:
            return (self.batch(data, self.index) for data in self.data)
        else:
            self.index = -1
            raise StopIteration()

import ipdb
import numpy as np
import theano.tensor as T
from cle.cle.data import DesignMatrix


class MNIST(DesignMatrix):
    """
    MNIST batch provider

    Parameters
    ----------
    .. todo::
    """
    def load(self, path):
        data = np.load(path)
        if self.name == 'train':
            return data[0]
        elif self.name == 'valid':
            return data[1]
        elif self.name == 'test':
            return data[2]

    def theano_vars(self):
        return [T.fmatrix('x'), T.lvector('y')]

from typing import Any

import numpy as np
from numpy import ndarray, dtype, signedinteger

a: ndarray[Any, dtype[signedinteger[Any]]] = np.arange(15).reshape(3, 5)
print("shape={0}, ndim={1}, dtype={2}, itemsize={3}, size={4}".format(a.shape,a.ndim,a.dtype,a.itemsize,a.size))
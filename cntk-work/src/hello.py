# encoding:utf-8

import cntk
import numpy as np
from cntk.device import try_set_default_device, gpu

cntk.__version__

cntk.minus([1, 2, 3], [4, 5, 6]).eval()

x = cntk.input_variable(2)
y = cntk.input_variable(2)
x0 = np.asarray([[2., 1.]], dtype=np.float32)
y0 = np.asarray([[4., 6.]], dtype=np.float32)
cntk.squared_error(x, y).eval({x:x0, y:y0})

c = cntk.constant(3, shape=(2,3))
c.asarray()

try_set_default_device(gpu(0))

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.quantum_info import DensityMatrix

rho = DensityMatrix.from_label('-0')
print(rho.to_dict())


# In[2]:


import numpy as np
from qiskit.quantum_info import DensityMatrix

mat = np.zeros((9, 9))
mat[0, 0] = 0.25
mat[3, 3] = 0.25
mat[6, 6] = 0.25
mat[-1, -1] = 0.25
rho = DensityMatrix(mat, dims=(3, 3))
print(rho.to_dict())


# In[3]:


import numpy as np
from qiskit.quantum_info import DensityMatrix

mat = np.zeros((2 * 10, 2 * 10))
mat[0, 0] = 0.5
mat[-1, -1] = 0.5
rho = DensityMatrix(mat, dims=(2, 10))
print(rho.to_dict())


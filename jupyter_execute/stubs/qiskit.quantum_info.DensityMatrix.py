#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.quantum_info import DensityMatrix

rho = DensityMatrix.from_label('+0')

# Probabilities for measuring both qubits
probs = rho.probabilities()
print('probs: {}'.format(probs))

# Probabilities for measuring only qubit-0
probs_qubit_0 = rho.probabilities([0])
print('Qubit-0 probs: {}'.format(probs_qubit_0))

# Probabilities for measuring only qubit-1
probs_qubit_1 = rho.probabilities([1])
print('Qubit-1 probs: {}'.format(probs_qubit_1))


# In[2]:


from qiskit.quantum_info import DensityMatrix

rho = DensityMatrix.from_label('+0')

# Probabilities for measuring both qubits
probs = rho.probabilities([0, 1])
print('probs: {}'.format(probs))

# Probabilities for measuring both qubits
# but swapping qubits 0 and 1 in output
probs_swapped = rho.probabilities([1, 0])
print('Swapped probs: {}'.format(probs_swapped))


# In[3]:


from qiskit.quantum_info import DensityMatrix

rho = DensityMatrix.from_label('-0')
print(rho.to_dict())


# In[4]:


import numpy as np
from qiskit.quantum_info import DensityMatrix

mat = np.zeros((9, 9))
mat[0, 0] = 0.25
mat[3, 3] = 0.25
mat[6, 6] = 0.25
mat[-1, -1] = 0.25
rho = DensityMatrix(mat, dims=(3, 3))
print(rho.to_dict())


# In[5]:


import numpy as np
from qiskit.quantum_info import DensityMatrix

mat = np.zeros((2 * 10, 2 * 10))
mat[0, 0] = 0.5
mat[-1, -1] = 0.5
rho = DensityMatrix(mat, dims=(2, 10))
print(rho.to_dict())


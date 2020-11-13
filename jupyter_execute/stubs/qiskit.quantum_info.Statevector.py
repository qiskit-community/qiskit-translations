#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.quantum_info import Statevector

psi = Statevector.from_label('+0')

# Probabilities for measuring both qubits
probs = psi.probabilities()
print('probs: {}'.format(probs))

# Probabilities for measuring only qubit-0
probs_qubit_0 = psi.probabilities([0])
print('Qubit-0 probs: {}'.format(probs_qubit_0))

# Probabilities for measuring only qubit-1
probs_qubit_1 = psi.probabilities([1])
print('Qubit-1 probs: {}'.format(probs_qubit_1))


# In[2]:


from qiskit.quantum_info import Statevector

psi = Statevector.from_label('+0')

# Probabilities for measuring both qubits
probs = psi.probabilities([0, 1])
print('probs: {}'.format(probs))

# Probabilities for measuring both qubits
# but swapping qubits 0 and 1 in output
probs_swapped = psi.probabilities([1, 0])
print('Swapped probs: {}'.format(probs_swapped))


# In[3]:


from qiskit.quantum_info import Statevector

psi = Statevector.from_label('-0')
print(psi.to_dict())


# In[4]:


import numpy as np
from qiskit.quantum_info import Statevector

vec = np.zeros(9)
vec[0] = 1 / np.sqrt(2)
vec[-1] = 1 / np.sqrt(2)
psi = Statevector(vec, dims=(3, 3))
print(psi.to_dict())


# In[5]:


import numpy as np
from qiskit.quantum_info import Statevector

vec = np.zeros(2 * 10)
vec[0] = 1 / np.sqrt(2)
vec[-1] = 1 / np.sqrt(2)
psi = Statevector(vec, dims=(2, 10))
print(psi.to_dict())


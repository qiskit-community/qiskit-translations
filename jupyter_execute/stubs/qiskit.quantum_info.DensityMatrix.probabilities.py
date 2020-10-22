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


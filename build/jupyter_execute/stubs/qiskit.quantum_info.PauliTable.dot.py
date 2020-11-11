#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.quantum_info.operators import PauliTable

current = PauliTable.from_labels(['I', 'X'])
other =  PauliTable.from_labels(['Y', 'Z'])
print(current.dot(other))


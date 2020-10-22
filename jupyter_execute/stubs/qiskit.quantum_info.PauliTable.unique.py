#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.quantum_info.operators import PauliTable

pt = PauliTable.from_labels(['X', 'Y', 'X', 'I', 'I', 'Z', 'X', 'Z'])
unique = pt.unique()
print(unique)


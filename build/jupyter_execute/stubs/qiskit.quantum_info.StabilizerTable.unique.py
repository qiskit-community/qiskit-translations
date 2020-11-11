#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.quantum_info.operators import StabilizerTable

st = StabilizerTable.from_labels(['+X', '+I', '-I', '-X', '+X', '-X', '+I'])
unique = st.unique()
print(unique)


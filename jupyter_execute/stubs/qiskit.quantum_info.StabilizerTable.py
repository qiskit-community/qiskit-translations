#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.quantum_info.operators import StabilizerTable

current = StabilizerTable.from_labels(['+I', '-X'])
other =  StabilizerTable.from_labels(['+X', '-Z'])
print(current.compose(other))


# In[2]:


from qiskit.quantum_info.operators import StabilizerTable

current = StabilizerTable.from_labels(['+I', '-X'])
other =  StabilizerTable.from_labels(['+X', '-Z'])
print(current.dot(other))


# In[3]:


from qiskit.quantum_info.operators import StabilizerTable

current = StabilizerTable.from_labels(['+I', '-X'])
other =  StabilizerTable.from_labels(['-Y', '+Z'])
print(current.expand(other))


# In[4]:


from numpy.random import shuffle
from qiskit.quantum_info.operators import StabilizerTable

# 2-qubit labels
labels = ['+II', '+IX', '+IY', '+IZ', '+XI', '+XX', '+XY', '+XZ',
          '+YI', '+YX', '+YY', '+YZ', '+ZI', '+ZX', '+ZY', '+ZZ',
          '-II', '-IX', '-IY', '-IZ', '-XI', '-XX', '-XY', '-XZ',
          '-YI', '-YX', '-YY', '-YZ', '-ZI', '-ZX', '-ZY', '-ZZ']
# Shuffle Labels
shuffle(labels)
st = StabilizerTable.from_labels(labels)
print('Initial Ordering')
print(st)

# Lexicographic Ordering
srt = st.sort()
print('Lexicographically sorted')
print(srt)

# Weight Ordering
srt = st.sort(weight=True)
print('Weight sorted')
print(srt)


# In[5]:


from qiskit.quantum_info.operators import StabilizerTable

current = StabilizerTable.from_labels(['+I', '-X'])
other =  StabilizerTable.from_labels(['-Y', '+Z'])
print(current.tensor(other))


# In[6]:


from qiskit.quantum_info.operators import StabilizerTable

st = StabilizerTable.from_labels(['+X', '+I', '-I', '-X', '+X', '-X', '+I'])
unique = st.unique()
print(unique)


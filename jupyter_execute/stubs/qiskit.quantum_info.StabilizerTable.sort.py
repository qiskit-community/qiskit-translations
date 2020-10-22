#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


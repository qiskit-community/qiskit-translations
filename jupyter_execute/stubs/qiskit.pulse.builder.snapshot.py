#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse

with pulse.build() as pulse_prog:
    pulse.snapshot('first', 'statevector')


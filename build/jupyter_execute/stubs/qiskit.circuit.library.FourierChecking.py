#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import FourierChecking
import qiskit.tools.jupyter
f = [1, -1, -1, -1]
g = [1, 1, -1, -1]
circuit = FourierChecking(f, g)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


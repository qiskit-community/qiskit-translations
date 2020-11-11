#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import XOR
import qiskit.tools.jupyter
circuit = XOR(5, seed=42)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


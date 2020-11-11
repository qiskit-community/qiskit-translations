#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import HiddenLinearFunction
import qiskit.tools.jupyter
A = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
circuit = HiddenLinearFunction(A)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


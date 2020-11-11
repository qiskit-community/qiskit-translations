#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import InnerProduct
import qiskit.tools.jupyter
circuit = InnerProduct(5)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


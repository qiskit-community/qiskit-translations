#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import MCMTVChain, ZGate
import qiskit.tools.jupyter
circuit = MCMTVChain(ZGate(), 2, 2)
get_ipython().run_line_magic('circuit_library_info', 'circuit.decompose()')


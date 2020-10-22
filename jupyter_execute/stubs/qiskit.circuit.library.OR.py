#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import OR
import qiskit.tools.jupyter
circuit = OR(5)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


# In[2]:


from qiskit.circuit.library import OR
import qiskit.tools.jupyter
circuit = OR(5, flags=[-1, 0, 0, 1, 1])
get_ipython().run_line_magic('circuit_library_info', 'circuit')


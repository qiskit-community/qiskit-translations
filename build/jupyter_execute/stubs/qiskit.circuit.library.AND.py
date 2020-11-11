#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import AND
import qiskit.tools.jupyter
circuit = AND(5)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


# In[2]:


from qiskit.circuit.library import AND
import qiskit.tools.jupyter
circuit = AND(5, flags=[-1, 0, 0, 1, 1])
get_ipython().run_line_magic('circuit_library_info', 'circuit')


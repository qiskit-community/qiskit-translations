#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import QFT
import qiskit.tools.jupyter
circuit = QFT(4)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


# In[2]:


from qiskit.circuit.library import QFT
import qiskit.tools.jupyter
circuit = QFT(4).inverse()
get_ipython().run_line_magic('circuit_library_info', 'circuit')


# In[3]:


from qiskit.circuit.library import QFT
import qiskit.tools.jupyter
circuit = QFT(5, approximation_degree=2)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


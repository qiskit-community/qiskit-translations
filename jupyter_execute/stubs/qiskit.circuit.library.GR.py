#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import GR
import qiskit.tools.jupyter
import numpy as np
circuit = GR(num_qubits=3, theta=np.pi/4, phi=np.pi/2)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


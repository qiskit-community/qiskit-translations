#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import GRY
import qiskit.tools.jupyter
import numpy as np
circuit = GRY(num_qubits=3, theta=np.pi/4)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


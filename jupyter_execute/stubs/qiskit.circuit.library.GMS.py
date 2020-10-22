#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import GMS
import qiskit.tools.jupyter
import numpy as np
circuit = GMS(num_qubits=3, theta=[[0, np.pi/4, np.pi/8],
                                   [0, 0, np.pi/2],
                                   [0, 0, 0]])
get_ipython().run_line_magic('circuit_library_info', 'circuit.decompose()')


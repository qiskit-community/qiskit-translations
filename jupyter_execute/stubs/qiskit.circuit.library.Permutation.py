#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import Permutation
import qiskit.tools.jupyter
A = [2,4,3,0,1]
circuit = Permutation(5, A)
circuit.draw('mpl')


# In[2]:


from qiskit.circuit.library import Permutation
import qiskit.tools.jupyter
A = [2,4,3,0,1]
circuit = Permutation(5, A)
get_ipython().run_line_magic('circuit_library_info', 'circuit.decompose()')


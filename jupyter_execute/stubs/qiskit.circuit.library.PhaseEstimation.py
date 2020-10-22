#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import PhaseEstimation
import qiskit.tools.jupyter
unitary = QuantumCircuit(2)
unitary.x(0)
unitary.y(1)
circuit = PhaseEstimation(3, unitary)
get_ipython().run_line_magic('circuit_library_info', 'circuit')


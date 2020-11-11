#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
get_ipython().run_line_magic('matplotlib', 'inline')

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

state = Statevector.from_instruction(qc)
plot_bloch_multivector(state, title="New Bloch Multivector")


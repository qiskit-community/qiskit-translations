#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit
from qiskit.quantum_info import CNOTDihedral

circ = QuantumCircuit(3)
circ.cx(0, 1)
circ.x(2)
circ.t(1)
circ.t(1)
circ.t(1)
elem = CNOTDihedral(circ)

# Print the CNOTDihedral element
print(elem)


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import HGate

qr = QuantumRegister(3)
qc = QuantumCircuit(qr)
c3h_gate = HGate().control(2)
qc.append(c3h_gate, qr)
qc.draw()


# In[2]:


from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import HGate

qc1 = QuantumCircuit(2)
qc1.x(0)
qc1.h(1)
custom = qc1.to_gate().control(2)

qc2 = QuantumCircuit(4)
qc2.append(custom, [0, 3, 1, 2])
qc2.draw()


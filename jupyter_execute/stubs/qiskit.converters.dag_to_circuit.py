#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.dagcircuit import DAGCircuit
from qiskit.converters import circuit_to_dag
from qiskit.circuit.library.standard_gates import CHGate, U2Gate, CXGate
from qiskit.converters import dag_to_circuit
get_ipython().run_line_magic('matplotlib', 'inline')

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
circ = QuantumCircuit(q, c)
circ.h(q[0])
circ.cx(q[0], q[1])
circ.measure(q[0], c[0])
circ.rz(0.5, q[1]).c_if(c, 2)
dag = circuit_to_dag(circ)
circuit = dag_to_circuit(dag)
circuit.draw()


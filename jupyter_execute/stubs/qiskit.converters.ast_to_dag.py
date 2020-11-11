#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.converters import ast_to_dag
from qiskit import qasm, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import dag_drawer
get_ipython().run_line_magic('matplotlib', 'inline')

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
circ = QuantumCircuit(q, c)
circ.h(q[0])
circ.cx(q[0], q[1])
circ.measure(q[0], c[0])
circ.rz(0.5, q[1]).c_if(c, 2)
qasm_str = circ.qasm()
ast = qasm.Qasm(data=qasm_str).parse()
dag = ast_to_dag(ast)
dag_drawer(dag)


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit, BasicAer, execute
from qiskit.visualization import plot_histogram
get_ipython().run_line_magic('matplotlib', 'inline')

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend)
plot_histogram(job.result().get_counts(), color='midnightblue', title="New Histogram")


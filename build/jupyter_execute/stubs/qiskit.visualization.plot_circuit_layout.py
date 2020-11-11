#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.test.ibmq_mock import mock_get_backend
mock_get_backend('FakeVigo')


# In[2]:


import numpy as np
from qiskit import QuantumCircuit, IBMQ, transpile
from qiskit.visualization import plot_histogram, plot_gate_map, plot_circuit_layout
from qiskit.tools.monitor import job_monitor
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

IBMQ.load_account()

ghz = QuantumCircuit(3, 3)
ghz.h(0)
for idx in range(1,3):
    ghz.cx(0,idx)
ghz.measure(range(3), range(3))

provider = IBMQ.get_provider(hub='ibm-q')
backend = provider.get_backend('ibmq_vigo')
new_circ_lv3 = transpile(ghz, backend=backend, optimization_level=3)
plot_circuit_layout(new_circ_lv3, backend)


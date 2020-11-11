#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit, transpile, schedule
from qiskit.visualization.timeline import draw
from qiskit.test.mock import FakeAlmaden

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)

qc = transpile(qc, FakeAlmaden(), scheduling_method='alap')
draw(qc)


# In[2]:


from qiskit import QuantumCircuit, transpile, schedule
from qiskit.visualization.timeline import draw, IQXSimple
from qiskit.test.mock import FakeAlmaden

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)

qc = transpile(qc, FakeAlmaden(), scheduling_method='alap')
draw(qc, style=IQXSimple())


# In[3]:


from qiskit import QuantumCircuit, transpile, schedule
from qiskit.visualization.timeline import draw, IQXDebugging
from qiskit.test.mock import FakeAlmaden

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)

qc = transpile(qc, FakeAlmaden(), scheduling_method='alap')
draw(qc, style=IQXDebugging())


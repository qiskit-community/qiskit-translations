#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit, transpile, schedule
from qiskit.visualization.pulse_v2 import draw
from qiskit.test.mock import FakeAlmaden

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
qc = transpile(qc, FakeAlmaden())
sched = schedule(qc, FakeAlmaden())

draw(sched, backend=FakeAlmaden())


# In[2]:


from qiskit import QuantumCircuit, transpile, schedule
from qiskit.visualization.pulse_v2 import draw, IQXSimple
from qiskit.test.mock import FakeAlmaden

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
qc = transpile(qc, FakeAlmaden())
sched = schedule(qc, FakeAlmaden())

draw(sched, style=IQXSimple(), backend=FakeAlmaden())


# In[3]:


from qiskit import QuantumCircuit, transpile, schedule
from qiskit.visualization.pulse_v2 import draw, IQXDebugging
from qiskit.test.mock import FakeAlmaden

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
qc = transpile(qc, FakeAlmaden())
sched = schedule(qc, FakeAlmaden())

draw(sched, style=IQXDebugging(), backend=FakeAlmaden())


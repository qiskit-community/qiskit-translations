#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import circuit, pulse, schedule, transpile
from qiskit.test.mock import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()

qc = circuit.QuantumCircuit(2)
qc.cx(0, 1)
qc_transpiled = transpile(qc, optimization_level=3)
sched = schedule(qc_transpiled, backend)

with pulse.build(backend) as pulse_prog:
        pulse.call(sched)
        pulse.call(qc)


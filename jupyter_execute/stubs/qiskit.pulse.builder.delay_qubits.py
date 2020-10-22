#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse
from qiskit.test.mock import FakeOpenPulse3Q

backend = FakeOpenPulse3Q()

with pulse.build(backend) as pulse_prog:
    # Delay for 100 cycles on qubits 0, 1 and 2.
    regs = pulse.delay_qubits(100, 0, 1, 2)


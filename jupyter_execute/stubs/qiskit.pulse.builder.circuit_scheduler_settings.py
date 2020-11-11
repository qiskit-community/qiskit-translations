#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse
from qiskit.test.mock import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()

with pulse.build(backend):
    print(pulse.active_circuit_scheduler_settings())
    with pulse.circuit_scheduler_settings(method='alap'):
        print(pulse.active_circuit_scheduler_settings())


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse
from qiskit.test.mock import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()

circuit_scheduler_settings = {'method': 'alap'}

with pulse.build(
        backend,
        default_circuit_scheduler_settings=circuit_scheduler_settings):
    print(pulse.active_circuit_scheduler_settings())


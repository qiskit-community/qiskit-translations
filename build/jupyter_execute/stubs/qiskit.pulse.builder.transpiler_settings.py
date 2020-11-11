#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse
from qiskit.test.mock import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()

with pulse.build(backend):
    print(pulse.active_transpiler_settings())
    with pulse.transpiler_settings(optimization_level=3):
        print(pulse.active_transpiler_settings())


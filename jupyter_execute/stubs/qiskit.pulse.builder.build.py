#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import execute, pulse
from qiskit.test.mock import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()

d0 = pulse.DriveChannel(0)

with pulse.build() as pulse_prog:
    pulse.play(pulse.Constant(100, 0.5), d0)


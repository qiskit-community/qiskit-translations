#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse
from qiskit.test.mock import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()

with pulse.build(backend):
    assert pulse.drive_channel(0) == pulse.DriveChannel(0)


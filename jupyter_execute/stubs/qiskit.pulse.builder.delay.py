#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse

d0 = pulse.DriveChannel(0)

with pulse.build() as pulse_prog:
    pulse.delay(10, d0)


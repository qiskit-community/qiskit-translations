#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse

d0 = pulse.DriveChannel(0)

with pulse.build() as pulse_prog:
    pulse.set_frequency(1e9, d0)


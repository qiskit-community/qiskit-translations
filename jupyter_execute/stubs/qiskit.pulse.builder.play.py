#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse

d0 = pulse.DriveChannel(0)

with pulse.build() as pulse_prog:
    pulse.play(pulse.Constant(10, 1.0), d0)


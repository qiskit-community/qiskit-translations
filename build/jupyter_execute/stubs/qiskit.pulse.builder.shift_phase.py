#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

from qiskit import pulse

d0 = pulse.DriveChannel(0)

with pulse.build() as pulse_prog:
    pulse.shift_phase(math.pi, d0)


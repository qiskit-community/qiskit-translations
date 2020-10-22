#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

from qiskit import pulse

d0 = pulse.DriveChannel(0)

with pulse.build() as pulse_prog:
    with pulse.phase_offset(math.pi, d0):
        pulse.play(pulse.Constant(10, 1.0), d0)

assert len(pulse_prog.instructions) == 3


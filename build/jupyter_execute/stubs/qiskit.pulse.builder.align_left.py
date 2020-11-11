#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse

d0 = pulse.DriveChannel(0)
d1 = pulse.DriveChannel(1)

with pulse.build() as pulse_prog:
    with pulse.align_left():
        # this pulse will start at t=0
        pulse.play(pulse.Constant(100, 1.0), d0)
        # this pulse will start at t=0
        pulse.play(pulse.Constant(20, 1.0), d1)

assert pulse_prog.ch_start_time(d0) == pulse_prog.ch_start_time(d1)


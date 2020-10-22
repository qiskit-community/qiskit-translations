#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse

d0 = pulse.DriveChannel(0)
d1 = pulse.DriveChannel(1)
d2 = pulse.DriveChannel(2)

with pulse.build() as pulse_prog:
    # will be ignored due to internal grouping
    with pulse.align_left():
        pulse.play(pulse.Constant(10, 1.0), d0)
        with pulse.inline():
            with pulse.align_right():
                # this pulse will start at t=0
                pulse.play(pulse.Constant(100, 1.0), d1)
                # this pulse will also start at t=0
                pulse.play(pulse.Constant(20, 1.0), d2)

assert (pulse_prog.ch_start_time(d0) ==
        pulse_prog.ch_start_time(d1) ==
        pulse_prog.ch_start_time(d2))


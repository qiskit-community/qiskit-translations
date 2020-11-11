#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse
from qiskit.test.mock import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()

d0 = pulse.DriveChannel(0)
d1 = pulse.DriveChannel(1)

with pulse.build(backend) as barrier_pulse_prog:
    pulse.play(pulse.Constant(10, 1.0), d0)
    pulse.barrier(d0, d1)
    pulse.play(pulse.Constant(10, 1.0), d1)


# In[2]:


from qiskit.pulse import transforms

with pulse.build(backend) as aligned_pulse_prog:
    with pulse.align_sequential():
        pulse.play(pulse.Constant(10, 1.0), d0)
        pulse.play(pulse.Constant(10, 1.0), d1)

barrier_pulse_prog = transforms.remove_directives(barrier_pulse_prog)
assert barrier_pulse_prog == aligned_pulse_prog


# In[3]:


import math

d0 = pulse.DriveChannel(0)

with pulse.build(backend) as pulse_prog:
    with pulse.align_right():
        pulse.x(1)
        # Barrier qubit 1 and d0.
        pulse.barrier(1, d0)
        # Due to barrier this will play before the gate on qubit 1.
        pulse.play(pulse.Constant(10, 1.0), d0)
        # This will end at the same time as the pulse above due to
        # the barrier.
        pulse.x(1)


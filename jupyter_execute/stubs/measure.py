#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse
from qiskit.test.mock import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()

qubit = 0

with pulse.build(backend) as pulse_prog:
    # Do something to the qubit.
    qubit_drive_chan = pulse.drive_channel(0)
    pulse.play(pulse.Constant(100, 1.0), qubit_drive_chan)
    # Measure the qubit.
    reg = pulse.measure(qubit)


# In[2]:


with pulse.build(backend) as pulse_prog:
    pulse.play(pulse.Constant(100, 1.0), qubit_drive_chan)
    # Measure the qubit.
    mem0 = pulse.MemorySlot(0)
    reg = pulse.measure(qubit, mem0)

assert reg == mem0


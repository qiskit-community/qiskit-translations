#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse
from qiskit.pulse import transforms

with pulse.build() as sched:
    with pulse.align_sequential():
        pulse.play(pulse.Constant(10, 0.5), pulse.DriveChannel(0))
        pulse.play(pulse.Constant(10, 1.), pulse.MeasureChannel(0))
        pulse.acquire(20, pulse.AcquireChannel(0), pulse.MemorySlot(0))

sched_shifted = sched << 20

aligned_sched, aligned_sched_shifted = transforms.align_measures([sched, sched_shifted])

assert aligned_sched == aligned_sched_shifted


# In[2]:


aligned_sched, aligned_sched_shifted = transforms.align_measures(
    [sched, sched_shifted],
    align_all=False,
)

assert aligned_sched != aligned_sched_shifted


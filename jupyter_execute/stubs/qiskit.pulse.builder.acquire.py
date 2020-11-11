#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse

d0 = pulse.MeasureChannel(0)
mem0 = pulse.MemorySlot(0)

with pulse.build() as pulse_prog:
    pulse.acquire(100, d0, mem0)

    # measurement metadata
    kernel = pulse.configuration.Kernel('linear_discriminator')
    pulse.acquire(100, d0, mem0, kernel=kernel)


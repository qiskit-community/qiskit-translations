#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse

d0 = pulse.DriveChannel(0)
x90 = pulse.Gaussian(10, 0.1, 3)
x180 = pulse.Gaussian(10, 0.2, 3)

with pulse.build() as hahn_echo:
    with pulse.align_equispaced(duration=100):
        pulse.play(x90, d0)
        pulse.play(x180, d0)
        pulse.play(x90, d0)

hahn_echo.draw()


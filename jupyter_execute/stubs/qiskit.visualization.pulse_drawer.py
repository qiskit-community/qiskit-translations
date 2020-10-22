#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import qiskit
from qiskit import pulse
from qiskit.test.mock.backends.almaden import FakeAlmaden

inst_map = FakeAlmaden().defaults().instruction_schedule_map

sched = pulse.Schedule()
sched += inst_map.get('u3', 0, np.pi, 0, np.pi)
sched += inst_map.get('measure', list(range(20))) << sched.duration

channels = [pulse.DriveChannel(0), pulse.MeasureChannel(0)]
scales = {pulse.DriveChannel(0): 10}

qiskit.visualization.pulse_drawer(sched,
                                  channels=channels,
                                  plot_range=(0, 1000),
                                  label=True,
                                  channel_scales=scales)


# In[2]:


import numpy as np
import qiskit
from qiskit import pulse
from qiskit.test.mock.backends.almaden import FakeAlmaden

inst_map = FakeAlmaden().defaults().instruction_schedule_map

sched = pulse.Schedule()
sched += inst_map.get('u3', 0, np.pi, 0, np.pi)
sched += inst_map.get('measure', list(range(20))) << sched.duration

# setup style sheet
my_style = qiskit.visualization.SchedStyle(
    figsize = (10, 5),
    bg_color='w',
    d_ch_color = ['#32cd32', '#556b2f'])

channels = [pulse.DriveChannel(0), pulse.MeasureChannel(0)]
scales = {pulse.DriveChannel(0): 10}

qiskit.visualization.pulse_drawer(sched, style=my_style,
                                  channels=channels,
                                  plot_range=(0, 1000),
                                  label=True,
                                  channel_scales=scales)


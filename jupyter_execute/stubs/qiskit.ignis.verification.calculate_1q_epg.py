#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pprint
import qiskit.ignis.verification.randomized_benchmarking as rb

# assuming we ran 1Q RB experiment for qubit 0
gpc = {0: {'cx': 0, 'u1': 0.13, 'u2': 0.31, 'u3': 0.51}}
epc = 1.5e-3

# calculate 1Q EPGs
epgs = rb.rb_utils.calculate_1q_epg(gate_per_cliff=gpc, epc_1q=epc, qubit=0)
pprint.pprint(epgs)


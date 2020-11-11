#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qiskit.ignis.verification.randomized_benchmarking as rb

# gate counts of your 1Q RB experiment
gpc = {0: {'cx': 0, 'u1': 0.13, 'u2': 0.31, 'u3': 0.51}}

# EPGs from error model
epgs_q0 = {'u1': 0, 'u2': 0.001, 'u3': 0.002}

# calculate 1Q EPC
epc = rb.rb_utils.calculate_1q_epc(
    gate_per_cliff=gpc,
    epg_1q=epgs_q0,
    qubit=0)

print(epc)


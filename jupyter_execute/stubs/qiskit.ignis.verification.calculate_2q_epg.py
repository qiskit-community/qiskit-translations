#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qiskit.ignis.verification.randomized_benchmarking as rb

# assuming we ran 1Q RB experiment for qubit 0 and qubit 1
gpc = {0: {'cx': 0, 'u1': 0.13, 'u2': 0.31, 'u3': 0.51},
       1: {'cx': 0, 'u1': 0.10, 'u2': 0.33, 'u3': 0.51}}
epc_q0 = 1.5e-3
epc_q1 = 5.8e-4

# calculate 1Q EPGs
epgs_q0 = rb.rb_utils.calculate_1q_epg(gate_per_cliff=gpc, epc_1q=epc_q0, qubit=0)
epgs_q1 = rb.rb_utils.calculate_1q_epg(gate_per_cliff=gpc, epc_1q=epc_q1, qubit=1)

# assuming we ran 2Q RB experiment for qubit 0 and qubit 1
gpc = {0: {'cx': 1.49, 'u1': 0.25, 'u2': 0.95, 'u3': 0.56},
       1: {'cx': 1.49, 'u1': 0.24, 'u2': 0.98, 'u3': 0.49}}
epc = 2.4e-2

# calculate 2Q EPG
epg_no_comp = rb.rb_utils.calculate_2q_epg(
    gate_per_cliff=gpc,
    epc_2q=epc,
    qubit_pair=[0, 1])

epg_comp = rb.rb_utils.calculate_2q_epg(
    gate_per_cliff=gpc,
    epc_2q=epc,
    qubit_pair=[0, 1],
    list_epgs_1q=[epgs_q0, epgs_q1])

print('EPG without `list_epgs_1q`: %f, with `list_epgs_1q`: %f' % (epg_no_comp, epg_comp))


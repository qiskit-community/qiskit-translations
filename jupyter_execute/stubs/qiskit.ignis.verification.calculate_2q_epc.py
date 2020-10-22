#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qiskit.ignis.verification.randomized_benchmarking as rb

# gate counts of your 2Q RB experiment
gpc = {0: {'cx': 1.49, 'u1': 0.25, 'u2': 0.95, 'u3': 0.56},
       1: {'cx': 1.49, 'u1': 0.24, 'u2': 0.98, 'u3': 0.49}}

# EPGs from error model
epgs_q0 = {'u1': 0, 'u2': 0.001, 'u3': 0.002}
epgs_q1 = {'u1': 0, 'u2': 0.002, 'u3': 0.004}
epg_q01 = 0.03

# calculate 2Q EPC
epc_2q = rb.rb_utils.calculate_2q_epc(
    gate_per_cliff=gpc,
    epg_2q=epg_q01,
    qubit_pair=[0, 1],
    list_epgs_1q=[epgs_q0, epgs_q1])

# calculate EPC according to the definition
fid = 1
for qubit in (0, 1):
    for epgs in (epgs_q0, epgs_q1):
        for gate, val in epgs.items():
            fid *= (1 - val) ** gpc[qubit][gate]
fid *= (1 - epg_q01) ** 1.49
epc = 1 - fid

print('Total sequence EPC: %f, 2Q gate contribution: %f' % (epc, epc_2q))


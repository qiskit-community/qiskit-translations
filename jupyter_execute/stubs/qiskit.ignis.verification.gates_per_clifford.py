#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pprint
import qiskit
import qiskit.ignis.verification.randomized_benchmarking as rb
from qiskit.test.mock.backends import FakeAlmaden

rb_circs_list, xdata = rb.randomized_benchmarking_seq(
    nseeds=5,
    length_vector=[1, 20, 50, 100],
    rb_pattern=[[0, 1]])
basis = FakeAlmaden().configuration().basis_gates

# transpile
transpiled_circuits_list = []
for rb_circs in rb_circs_list:
    rb_circs_transpiled = qiskit.transpile(rb_circs, basis_gates=basis)
    transpiled_circuits_list.append(rb_circs_transpiled)

# count gate per Clifford
ngates = rb.rb_utils.gates_per_clifford(
    transpiled_circuits_list=transpiled_circuits_list,
    clifford_lengths=xdata[0],
    basis=basis, qubits=[0, 1])

pprint.pprint(ngates)


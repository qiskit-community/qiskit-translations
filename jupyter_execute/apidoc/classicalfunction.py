#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit import classical_function,  Int1

@classical_function
def grover_oracle(a: Int1, b: Int1, c: Int1, d: Int1) -> Int1:
    return (not a and b and not c and d)

quantum_circuit = grover_oracle.synth()
quantum_circuit.draw()


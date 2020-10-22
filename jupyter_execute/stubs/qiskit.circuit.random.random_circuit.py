#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.random import random_circuit

circ = random_circuit(2, 2, measure=True)
circ.draw(output='mpl')


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *


# In[2]:


qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(2, 'zx_meas')
qc = QuantumCircuit(qr,cr)
qc.reset(range(3))
qc.barrier()
qc.h(1)
qc.cx([1,0],[2,1])
qc.h(0)
qc.barrier()
qc.measure([0,1], [0,1])
qc.barrier()
qc.z(2).c_if(cr, 1)
qc.x(2).c_if(cr, 2)


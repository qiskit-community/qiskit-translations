#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.visualization import plot_bloch_vector
get_ipython().run_line_magic('matplotlib', 'inline')

plot_bloch_vector([0,1,0], title="New Bloch Sphere")


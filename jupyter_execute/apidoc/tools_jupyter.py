#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from qiskit.tools.parallel import parallel_map
import qiskit.tools.jupyter

get_ipython().run_line_magic('qiskit_progress_bar', '')
parallel_map(np.sin, np.linspace(0,10,100));


# In[2]:


import qiskit.tools.jupyter
get_ipython().run_line_magic('qiskit_version_table', '')


# In[3]:


import qiskit.tools.jupyter
get_ipython().run_line_magic('qiskit_copyright', '')


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import GraphState
import qiskit.tools.jupyter
import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])
adjmat = nx.adjacency_matrix(G)
circuit = GraphState(adjmat.toarray())
get_ipython().run_line_magic('circuit_library_info', 'circuit')


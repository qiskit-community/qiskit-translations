#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from qiskit.algorithms import NumPyLinearSolver
from qiskit.algorithms.linear_solvers.matrices import TridiagonalToeplitz
from qiskit.algorithms.linear_solvers.observables import MatrixFunctional

matrix = TridiagonalToeplitz(2, 1, 1 / 3, trotter_steps=2)
right_hand_side = [1.0, -2.1, 3.2, -4.3]
observable = MatrixFunctional(1, 1 / 2)
rhs = right_hand_side / np.linalg.norm(right_hand_side)

np_solver = NumPyLinearSolver()
solution = np_solver.solve(matrix, rhs, observable)
result = solution.observable


import numpy as np
from qiskit.tools.parallel import parallel_map
import qiskit.tools.jupyter

%qiskit_progress_bar
parallel_map(np.sin, np.linspace(0,10,100));

import qiskit.tools.jupyter
%qiskit_version_table

import qiskit.tools.jupyter
%qiskit_copyright
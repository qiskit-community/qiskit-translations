qiskit.circuit.library.QAOAAnsatz
=================================

.. currentmodule:: qiskit.circuit.library

.. autoclass:: QAOAAnsatz

   
   .. automethod:: __init__

   
   .. rubric:: Methods

   .. autosummary::
   
      ~QAOAAnsatz.__init__
      ~QAOAAnsatz.add_bits
      ~QAOAAnsatz.add_calibration
      ~QAOAAnsatz.add_register
      ~QAOAAnsatz.append
      ~QAOAAnsatz.assign_parameters
      ~QAOAAnsatz.barrier
      ~QAOAAnsatz.bind_parameters
      ~QAOAAnsatz.cast
      ~QAOAAnsatz.cbit_argument_conversion
      ~QAOAAnsatz.ccx
      ~QAOAAnsatz.ch
      ~QAOAAnsatz.cls_instances
      ~QAOAAnsatz.cls_prefix
      ~QAOAAnsatz.cnot
      ~QAOAAnsatz.combine
      ~QAOAAnsatz.compose
      ~QAOAAnsatz.control
      ~QAOAAnsatz.copy
      ~QAOAAnsatz.count_ops
      ~QAOAAnsatz.cp
      ~QAOAAnsatz.crx
      ~QAOAAnsatz.cry
      ~QAOAAnsatz.crz
      ~QAOAAnsatz.cswap
      ~QAOAAnsatz.csx
      ~QAOAAnsatz.cu
      ~QAOAAnsatz.cu1
      ~QAOAAnsatz.cu3
      ~QAOAAnsatz.cx
      ~QAOAAnsatz.cy
      ~QAOAAnsatz.cz
      ~QAOAAnsatz.dcx
      ~QAOAAnsatz.decompose
      ~QAOAAnsatz.delay
      ~QAOAAnsatz.depth
      ~QAOAAnsatz.diagonal
      ~QAOAAnsatz.draw
      ~QAOAAnsatz.ecr
      ~QAOAAnsatz.extend
      ~QAOAAnsatz.fredkin
      ~QAOAAnsatz.from_qasm_file
      ~QAOAAnsatz.from_qasm_str
      ~QAOAAnsatz.h
      ~QAOAAnsatz.hamiltonian
      ~QAOAAnsatz.has_register
      ~QAOAAnsatz.i
      ~QAOAAnsatz.id
      ~QAOAAnsatz.initialize
      ~QAOAAnsatz.inverse
      ~QAOAAnsatz.iso
      ~QAOAAnsatz.isometry
      ~QAOAAnsatz.iswap
      ~QAOAAnsatz.mcp
      ~QAOAAnsatz.mcrx
      ~QAOAAnsatz.mcry
      ~QAOAAnsatz.mcrz
      ~QAOAAnsatz.mct
      ~QAOAAnsatz.mcu1
      ~QAOAAnsatz.mcx
      ~QAOAAnsatz.measure
      ~QAOAAnsatz.measure_active
      ~QAOAAnsatz.measure_all
      ~QAOAAnsatz.ms
      ~QAOAAnsatz.num_connected_components
      ~QAOAAnsatz.num_nonlocal_gates
      ~QAOAAnsatz.num_tensor_factors
      ~QAOAAnsatz.num_unitary_factors
      ~QAOAAnsatz.p
      ~QAOAAnsatz.pauli
      ~QAOAAnsatz.power
      ~QAOAAnsatz.qasm
      ~QAOAAnsatz.qbit_argument_conversion
      ~QAOAAnsatz.qubit_duration
      ~QAOAAnsatz.qubit_start_time
      ~QAOAAnsatz.qubit_stop_time
      ~QAOAAnsatz.r
      ~QAOAAnsatz.rcccx
      ~QAOAAnsatz.rccx
      ~QAOAAnsatz.remove_final_measurements
      ~QAOAAnsatz.repeat
      ~QAOAAnsatz.reset
      ~QAOAAnsatz.reverse_bits
      ~QAOAAnsatz.reverse_ops
      ~QAOAAnsatz.rv
      ~QAOAAnsatz.rx
      ~QAOAAnsatz.rxx
      ~QAOAAnsatz.ry
      ~QAOAAnsatz.ryy
      ~QAOAAnsatz.rz
      ~QAOAAnsatz.rzx
      ~QAOAAnsatz.rzz
      ~QAOAAnsatz.s
      ~QAOAAnsatz.save_amplitudes
      ~QAOAAnsatz.save_amplitudes_squared
      ~QAOAAnsatz.save_density_matrix
      ~QAOAAnsatz.save_expectation_value
      ~QAOAAnsatz.save_expectation_value_variance
      ~QAOAAnsatz.save_matrix_product_state
      ~QAOAAnsatz.save_probabilities
      ~QAOAAnsatz.save_probabilities_dict
      ~QAOAAnsatz.save_stabilizer
      ~QAOAAnsatz.save_state
      ~QAOAAnsatz.save_statevector
      ~QAOAAnsatz.save_statevector_dict
      ~QAOAAnsatz.save_superop
      ~QAOAAnsatz.save_unitary
      ~QAOAAnsatz.sdg
      ~QAOAAnsatz.set_density_matrix
      ~QAOAAnsatz.set_matrix_product_state
      ~QAOAAnsatz.set_stabilizer
      ~QAOAAnsatz.set_statevector
      ~QAOAAnsatz.set_superop
      ~QAOAAnsatz.set_unitary
      ~QAOAAnsatz.size
      ~QAOAAnsatz.snapshot
      ~QAOAAnsatz.snapshot_density_matrix
      ~QAOAAnsatz.snapshot_expectation_value
      ~QAOAAnsatz.snapshot_probabilities
      ~QAOAAnsatz.snapshot_stabilizer
      ~QAOAAnsatz.snapshot_statevector
      ~QAOAAnsatz.squ
      ~QAOAAnsatz.swap
      ~QAOAAnsatz.sx
      ~QAOAAnsatz.sxdg
      ~QAOAAnsatz.t
      ~QAOAAnsatz.tdg
      ~QAOAAnsatz.tensor
      ~QAOAAnsatz.to_gate
      ~QAOAAnsatz.to_instruction
      ~QAOAAnsatz.toffoli
      ~QAOAAnsatz.u
      ~QAOAAnsatz.u1
      ~QAOAAnsatz.u2
      ~QAOAAnsatz.u3
      ~QAOAAnsatz.uc
      ~QAOAAnsatz.ucrx
      ~QAOAAnsatz.ucry
      ~QAOAAnsatz.ucrz
      ~QAOAAnsatz.unitary
      ~QAOAAnsatz.width
      ~QAOAAnsatz.x
      ~QAOAAnsatz.y
      ~QAOAAnsatz.z
   
   

   
   
   .. rubric:: Attributes

   .. autosummary::
   
      ~QAOAAnsatz.ancillas
      ~QAOAAnsatz.calibrations
      ~QAOAAnsatz.clbits
      ~QAOAAnsatz.cost_operator
      ~QAOAAnsatz.data
      ~QAOAAnsatz.extension_lib
      ~QAOAAnsatz.global_phase
      ~QAOAAnsatz.header
      ~QAOAAnsatz.initial_state
      ~QAOAAnsatz.instances
      ~QAOAAnsatz.metadata
      ~QAOAAnsatz.mixer_operator
      ~QAOAAnsatz.num_ancillas
      ~QAOAAnsatz.num_clbits
      ~QAOAAnsatz.num_parameters
      ~QAOAAnsatz.num_qubits
      ~QAOAAnsatz.parameter_bounds
      ~QAOAAnsatz.parameters
      ~QAOAAnsatz.prefix
      ~QAOAAnsatz.qregs
      ~QAOAAnsatz.qubits
      ~QAOAAnsatz.reps
   
   
qiskit.circuit.library.PauliFeatureMap
======================================

.. currentmodule:: qiskit.circuit.library

.. autoclass:: PauliFeatureMap

   
   .. automethod:: __init__

   
   .. rubric:: Methods

   .. autosummary::
   
      ~PauliFeatureMap.__init__
      ~PauliFeatureMap.add_bits
      ~PauliFeatureMap.add_calibration
      ~PauliFeatureMap.add_layer
      ~PauliFeatureMap.add_register
      ~PauliFeatureMap.append
      ~PauliFeatureMap.assign_parameters
      ~PauliFeatureMap.barrier
      ~PauliFeatureMap.bind_parameters
      ~PauliFeatureMap.cast
      ~PauliFeatureMap.cbit_argument_conversion
      ~PauliFeatureMap.ccx
      ~PauliFeatureMap.ch
      ~PauliFeatureMap.cls_instances
      ~PauliFeatureMap.cls_prefix
      ~PauliFeatureMap.cnot
      ~PauliFeatureMap.combine
      ~PauliFeatureMap.compose
      ~PauliFeatureMap.control
      ~PauliFeatureMap.copy
      ~PauliFeatureMap.count_ops
      ~PauliFeatureMap.cp
      ~PauliFeatureMap.crx
      ~PauliFeatureMap.cry
      ~PauliFeatureMap.crz
      ~PauliFeatureMap.cswap
      ~PauliFeatureMap.csx
      ~PauliFeatureMap.cu
      ~PauliFeatureMap.cu1
      ~PauliFeatureMap.cu3
      ~PauliFeatureMap.cx
      ~PauliFeatureMap.cy
      ~PauliFeatureMap.cz
      ~PauliFeatureMap.dcx
      ~PauliFeatureMap.decompose
      ~PauliFeatureMap.delay
      ~PauliFeatureMap.depth
      ~PauliFeatureMap.diagonal
      ~PauliFeatureMap.draw
      ~PauliFeatureMap.ecr
      ~PauliFeatureMap.extend
      ~PauliFeatureMap.fredkin
      ~PauliFeatureMap.from_qasm_file
      ~PauliFeatureMap.from_qasm_str
      ~PauliFeatureMap.get_entangler_map
      ~PauliFeatureMap.get_unentangled_qubits
      ~PauliFeatureMap.h
      ~PauliFeatureMap.hamiltonian
      ~PauliFeatureMap.has_register
      ~PauliFeatureMap.i
      ~PauliFeatureMap.id
      ~PauliFeatureMap.initialize
      ~PauliFeatureMap.inverse
      ~PauliFeatureMap.iso
      ~PauliFeatureMap.isometry
      ~PauliFeatureMap.iswap
      ~PauliFeatureMap.mcp
      ~PauliFeatureMap.mcrx
      ~PauliFeatureMap.mcry
      ~PauliFeatureMap.mcrz
      ~PauliFeatureMap.mct
      ~PauliFeatureMap.mcu1
      ~PauliFeatureMap.mcx
      ~PauliFeatureMap.measure
      ~PauliFeatureMap.measure_active
      ~PauliFeatureMap.measure_all
      ~PauliFeatureMap.ms
      ~PauliFeatureMap.num_connected_components
      ~PauliFeatureMap.num_nonlocal_gates
      ~PauliFeatureMap.num_tensor_factors
      ~PauliFeatureMap.num_unitary_factors
      ~PauliFeatureMap.p
      ~PauliFeatureMap.pauli
      ~PauliFeatureMap.pauli_block
      ~PauliFeatureMap.pauli_evolution
      ~PauliFeatureMap.power
      ~PauliFeatureMap.print_settings
      ~PauliFeatureMap.qasm
      ~PauliFeatureMap.qbit_argument_conversion
      ~PauliFeatureMap.qubit_duration
      ~PauliFeatureMap.qubit_start_time
      ~PauliFeatureMap.qubit_stop_time
      ~PauliFeatureMap.r
      ~PauliFeatureMap.rcccx
      ~PauliFeatureMap.rccx
      ~PauliFeatureMap.remove_final_measurements
      ~PauliFeatureMap.repeat
      ~PauliFeatureMap.reset
      ~PauliFeatureMap.reverse_bits
      ~PauliFeatureMap.reverse_ops
      ~PauliFeatureMap.rv
      ~PauliFeatureMap.rx
      ~PauliFeatureMap.rxx
      ~PauliFeatureMap.ry
      ~PauliFeatureMap.ryy
      ~PauliFeatureMap.rz
      ~PauliFeatureMap.rzx
      ~PauliFeatureMap.rzz
      ~PauliFeatureMap.s
      ~PauliFeatureMap.save_amplitudes
      ~PauliFeatureMap.save_amplitudes_squared
      ~PauliFeatureMap.save_density_matrix
      ~PauliFeatureMap.save_expectation_value
      ~PauliFeatureMap.save_expectation_value_variance
      ~PauliFeatureMap.save_matrix_product_state
      ~PauliFeatureMap.save_probabilities
      ~PauliFeatureMap.save_probabilities_dict
      ~PauliFeatureMap.save_stabilizer
      ~PauliFeatureMap.save_state
      ~PauliFeatureMap.save_statevector
      ~PauliFeatureMap.save_statevector_dict
      ~PauliFeatureMap.save_superop
      ~PauliFeatureMap.save_unitary
      ~PauliFeatureMap.sdg
      ~PauliFeatureMap.set_density_matrix
      ~PauliFeatureMap.set_matrix_product_state
      ~PauliFeatureMap.set_stabilizer
      ~PauliFeatureMap.set_statevector
      ~PauliFeatureMap.set_superop
      ~PauliFeatureMap.set_unitary
      ~PauliFeatureMap.size
      ~PauliFeatureMap.snapshot
      ~PauliFeatureMap.snapshot_density_matrix
      ~PauliFeatureMap.snapshot_expectation_value
      ~PauliFeatureMap.snapshot_probabilities
      ~PauliFeatureMap.snapshot_stabilizer
      ~PauliFeatureMap.snapshot_statevector
      ~PauliFeatureMap.squ
      ~PauliFeatureMap.swap
      ~PauliFeatureMap.sx
      ~PauliFeatureMap.sxdg
      ~PauliFeatureMap.t
      ~PauliFeatureMap.tdg
      ~PauliFeatureMap.tensor
      ~PauliFeatureMap.to_gate
      ~PauliFeatureMap.to_instruction
      ~PauliFeatureMap.toffoli
      ~PauliFeatureMap.u
      ~PauliFeatureMap.u1
      ~PauliFeatureMap.u2
      ~PauliFeatureMap.u3
      ~PauliFeatureMap.uc
      ~PauliFeatureMap.ucrx
      ~PauliFeatureMap.ucry
      ~PauliFeatureMap.ucrz
      ~PauliFeatureMap.unitary
      ~PauliFeatureMap.width
      ~PauliFeatureMap.x
      ~PauliFeatureMap.y
      ~PauliFeatureMap.z
   
   

   
   
   .. rubric:: Attributes

   .. autosummary::
   
      ~PauliFeatureMap.alpha
      ~PauliFeatureMap.ancillas
      ~PauliFeatureMap.calibrations
      ~PauliFeatureMap.clbits
      ~PauliFeatureMap.data
      ~PauliFeatureMap.entanglement
      ~PauliFeatureMap.entanglement_blocks
      ~PauliFeatureMap.extension_lib
      ~PauliFeatureMap.feature_dimension
      ~PauliFeatureMap.global_phase
      ~PauliFeatureMap.header
      ~PauliFeatureMap.initial_state
      ~PauliFeatureMap.insert_barriers
      ~PauliFeatureMap.instances
      ~PauliFeatureMap.metadata
      ~PauliFeatureMap.num_ancillas
      ~PauliFeatureMap.num_clbits
      ~PauliFeatureMap.num_layers
      ~PauliFeatureMap.num_parameters
      ~PauliFeatureMap.num_parameters_settable
      ~PauliFeatureMap.num_qubits
      ~PauliFeatureMap.ordered_parameters
      ~PauliFeatureMap.parameter_bounds
      ~PauliFeatureMap.parameters
      ~PauliFeatureMap.paulis
      ~PauliFeatureMap.preferred_init_points
      ~PauliFeatureMap.prefix
      ~PauliFeatureMap.qregs
      ~PauliFeatureMap.qubits
      ~PauliFeatureMap.reps
      ~PauliFeatureMap.rotation_blocks
   
   
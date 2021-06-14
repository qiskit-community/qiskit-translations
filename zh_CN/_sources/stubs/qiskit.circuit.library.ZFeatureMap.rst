qiskit.circuit.library.ZFeatureMap
==================================

.. currentmodule:: qiskit.circuit.library

.. autoclass:: ZFeatureMap

   
   .. automethod:: __init__

   
   .. rubric:: Methods

   .. autosummary::
   
      ~ZFeatureMap.__init__
      ~ZFeatureMap.add_bits
      ~ZFeatureMap.add_calibration
      ~ZFeatureMap.add_layer
      ~ZFeatureMap.add_register
      ~ZFeatureMap.append
      ~ZFeatureMap.assign_parameters
      ~ZFeatureMap.barrier
      ~ZFeatureMap.bind_parameters
      ~ZFeatureMap.cast
      ~ZFeatureMap.cbit_argument_conversion
      ~ZFeatureMap.ccx
      ~ZFeatureMap.ch
      ~ZFeatureMap.cls_instances
      ~ZFeatureMap.cls_prefix
      ~ZFeatureMap.cnot
      ~ZFeatureMap.combine
      ~ZFeatureMap.compose
      ~ZFeatureMap.control
      ~ZFeatureMap.copy
      ~ZFeatureMap.count_ops
      ~ZFeatureMap.cp
      ~ZFeatureMap.crx
      ~ZFeatureMap.cry
      ~ZFeatureMap.crz
      ~ZFeatureMap.cswap
      ~ZFeatureMap.csx
      ~ZFeatureMap.cu
      ~ZFeatureMap.cu1
      ~ZFeatureMap.cu3
      ~ZFeatureMap.cx
      ~ZFeatureMap.cy
      ~ZFeatureMap.cz
      ~ZFeatureMap.dcx
      ~ZFeatureMap.decompose
      ~ZFeatureMap.delay
      ~ZFeatureMap.depth
      ~ZFeatureMap.diagonal
      ~ZFeatureMap.draw
      ~ZFeatureMap.ecr
      ~ZFeatureMap.extend
      ~ZFeatureMap.fredkin
      ~ZFeatureMap.from_qasm_file
      ~ZFeatureMap.from_qasm_str
      ~ZFeatureMap.get_entangler_map
      ~ZFeatureMap.get_unentangled_qubits
      ~ZFeatureMap.h
      ~ZFeatureMap.hamiltonian
      ~ZFeatureMap.has_register
      ~ZFeatureMap.i
      ~ZFeatureMap.id
      ~ZFeatureMap.initialize
      ~ZFeatureMap.inverse
      ~ZFeatureMap.iso
      ~ZFeatureMap.isometry
      ~ZFeatureMap.iswap
      ~ZFeatureMap.mcp
      ~ZFeatureMap.mcrx
      ~ZFeatureMap.mcry
      ~ZFeatureMap.mcrz
      ~ZFeatureMap.mct
      ~ZFeatureMap.mcu1
      ~ZFeatureMap.mcx
      ~ZFeatureMap.measure
      ~ZFeatureMap.measure_active
      ~ZFeatureMap.measure_all
      ~ZFeatureMap.ms
      ~ZFeatureMap.num_connected_components
      ~ZFeatureMap.num_nonlocal_gates
      ~ZFeatureMap.num_tensor_factors
      ~ZFeatureMap.num_unitary_factors
      ~ZFeatureMap.p
      ~ZFeatureMap.pauli
      ~ZFeatureMap.pauli_block
      ~ZFeatureMap.pauli_evolution
      ~ZFeatureMap.power
      ~ZFeatureMap.print_settings
      ~ZFeatureMap.qasm
      ~ZFeatureMap.qbit_argument_conversion
      ~ZFeatureMap.qubit_duration
      ~ZFeatureMap.qubit_start_time
      ~ZFeatureMap.qubit_stop_time
      ~ZFeatureMap.r
      ~ZFeatureMap.rcccx
      ~ZFeatureMap.rccx
      ~ZFeatureMap.remove_final_measurements
      ~ZFeatureMap.repeat
      ~ZFeatureMap.reset
      ~ZFeatureMap.reverse_bits
      ~ZFeatureMap.reverse_ops
      ~ZFeatureMap.rv
      ~ZFeatureMap.rx
      ~ZFeatureMap.rxx
      ~ZFeatureMap.ry
      ~ZFeatureMap.ryy
      ~ZFeatureMap.rz
      ~ZFeatureMap.rzx
      ~ZFeatureMap.rzz
      ~ZFeatureMap.s
      ~ZFeatureMap.save_amplitudes
      ~ZFeatureMap.save_amplitudes_squared
      ~ZFeatureMap.save_density_matrix
      ~ZFeatureMap.save_expectation_value
      ~ZFeatureMap.save_expectation_value_variance
      ~ZFeatureMap.save_matrix_product_state
      ~ZFeatureMap.save_probabilities
      ~ZFeatureMap.save_probabilities_dict
      ~ZFeatureMap.save_stabilizer
      ~ZFeatureMap.save_state
      ~ZFeatureMap.save_statevector
      ~ZFeatureMap.save_statevector_dict
      ~ZFeatureMap.save_superop
      ~ZFeatureMap.save_unitary
      ~ZFeatureMap.sdg
      ~ZFeatureMap.set_density_matrix
      ~ZFeatureMap.set_matrix_product_state
      ~ZFeatureMap.set_stabilizer
      ~ZFeatureMap.set_statevector
      ~ZFeatureMap.set_superop
      ~ZFeatureMap.set_unitary
      ~ZFeatureMap.size
      ~ZFeatureMap.snapshot
      ~ZFeatureMap.snapshot_density_matrix
      ~ZFeatureMap.snapshot_expectation_value
      ~ZFeatureMap.snapshot_probabilities
      ~ZFeatureMap.snapshot_stabilizer
      ~ZFeatureMap.snapshot_statevector
      ~ZFeatureMap.squ
      ~ZFeatureMap.swap
      ~ZFeatureMap.sx
      ~ZFeatureMap.sxdg
      ~ZFeatureMap.t
      ~ZFeatureMap.tdg
      ~ZFeatureMap.tensor
      ~ZFeatureMap.to_gate
      ~ZFeatureMap.to_instruction
      ~ZFeatureMap.toffoli
      ~ZFeatureMap.u
      ~ZFeatureMap.u1
      ~ZFeatureMap.u2
      ~ZFeatureMap.u3
      ~ZFeatureMap.uc
      ~ZFeatureMap.ucrx
      ~ZFeatureMap.ucry
      ~ZFeatureMap.ucrz
      ~ZFeatureMap.unitary
      ~ZFeatureMap.width
      ~ZFeatureMap.x
      ~ZFeatureMap.y
      ~ZFeatureMap.z
   
   

   
   
   .. rubric:: Attributes

   .. autosummary::
   
      ~ZFeatureMap.alpha
      ~ZFeatureMap.ancillas
      ~ZFeatureMap.calibrations
      ~ZFeatureMap.clbits
      ~ZFeatureMap.data
      ~ZFeatureMap.entanglement
      ~ZFeatureMap.entanglement_blocks
      ~ZFeatureMap.extension_lib
      ~ZFeatureMap.feature_dimension
      ~ZFeatureMap.global_phase
      ~ZFeatureMap.header
      ~ZFeatureMap.initial_state
      ~ZFeatureMap.insert_barriers
      ~ZFeatureMap.instances
      ~ZFeatureMap.metadata
      ~ZFeatureMap.num_ancillas
      ~ZFeatureMap.num_clbits
      ~ZFeatureMap.num_layers
      ~ZFeatureMap.num_parameters
      ~ZFeatureMap.num_parameters_settable
      ~ZFeatureMap.num_qubits
      ~ZFeatureMap.ordered_parameters
      ~ZFeatureMap.parameter_bounds
      ~ZFeatureMap.parameters
      ~ZFeatureMap.paulis
      ~ZFeatureMap.preferred_init_points
      ~ZFeatureMap.prefix
      ~ZFeatureMap.qregs
      ~ZFeatureMap.qubits
      ~ZFeatureMap.reps
      ~ZFeatureMap.rotation_blocks
   
   
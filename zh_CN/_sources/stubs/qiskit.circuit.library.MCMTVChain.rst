qiskit.circuit.library.MCMTVChain
=================================

.. currentmodule:: qiskit.circuit.library

.. autoclass:: MCMTVChain

   
   .. automethod:: __init__

   
   .. rubric:: Methods

   .. autosummary::
   
      ~MCMTVChain.__init__
      ~MCMTVChain.add_bits
      ~MCMTVChain.add_calibration
      ~MCMTVChain.add_register
      ~MCMTVChain.append
      ~MCMTVChain.assign_parameters
      ~MCMTVChain.barrier
      ~MCMTVChain.bind_parameters
      ~MCMTVChain.cast
      ~MCMTVChain.cbit_argument_conversion
      ~MCMTVChain.ccx
      ~MCMTVChain.ch
      ~MCMTVChain.cls_instances
      ~MCMTVChain.cls_prefix
      ~MCMTVChain.cnot
      ~MCMTVChain.combine
      ~MCMTVChain.compose
      ~MCMTVChain.control
      ~MCMTVChain.copy
      ~MCMTVChain.count_ops
      ~MCMTVChain.cp
      ~MCMTVChain.crx
      ~MCMTVChain.cry
      ~MCMTVChain.crz
      ~MCMTVChain.cswap
      ~MCMTVChain.csx
      ~MCMTVChain.cu
      ~MCMTVChain.cu1
      ~MCMTVChain.cu3
      ~MCMTVChain.cx
      ~MCMTVChain.cy
      ~MCMTVChain.cz
      ~MCMTVChain.dcx
      ~MCMTVChain.decompose
      ~MCMTVChain.delay
      ~MCMTVChain.depth
      ~MCMTVChain.diagonal
      ~MCMTVChain.draw
      ~MCMTVChain.ecr
      ~MCMTVChain.extend
      ~MCMTVChain.fredkin
      ~MCMTVChain.from_qasm_file
      ~MCMTVChain.from_qasm_str
      ~MCMTVChain.h
      ~MCMTVChain.hamiltonian
      ~MCMTVChain.has_register
      ~MCMTVChain.i
      ~MCMTVChain.id
      ~MCMTVChain.initialize
      ~MCMTVChain.inverse
      ~MCMTVChain.iso
      ~MCMTVChain.isometry
      ~MCMTVChain.iswap
      ~MCMTVChain.mcp
      ~MCMTVChain.mcrx
      ~MCMTVChain.mcry
      ~MCMTVChain.mcrz
      ~MCMTVChain.mct
      ~MCMTVChain.mcu1
      ~MCMTVChain.mcx
      ~MCMTVChain.measure
      ~MCMTVChain.measure_active
      ~MCMTVChain.measure_all
      ~MCMTVChain.ms
      ~MCMTVChain.num_connected_components
      ~MCMTVChain.num_nonlocal_gates
      ~MCMTVChain.num_tensor_factors
      ~MCMTVChain.num_unitary_factors
      ~MCMTVChain.p
      ~MCMTVChain.pauli
      ~MCMTVChain.power
      ~MCMTVChain.qasm
      ~MCMTVChain.qbit_argument_conversion
      ~MCMTVChain.qubit_duration
      ~MCMTVChain.qubit_start_time
      ~MCMTVChain.qubit_stop_time
      ~MCMTVChain.r
      ~MCMTVChain.rcccx
      ~MCMTVChain.rccx
      ~MCMTVChain.remove_final_measurements
      ~MCMTVChain.repeat
      ~MCMTVChain.reset
      ~MCMTVChain.reverse_bits
      ~MCMTVChain.reverse_ops
      ~MCMTVChain.rv
      ~MCMTVChain.rx
      ~MCMTVChain.rxx
      ~MCMTVChain.ry
      ~MCMTVChain.ryy
      ~MCMTVChain.rz
      ~MCMTVChain.rzx
      ~MCMTVChain.rzz
      ~MCMTVChain.s
      ~MCMTVChain.save_amplitudes
      ~MCMTVChain.save_amplitudes_squared
      ~MCMTVChain.save_density_matrix
      ~MCMTVChain.save_expectation_value
      ~MCMTVChain.save_expectation_value_variance
      ~MCMTVChain.save_matrix_product_state
      ~MCMTVChain.save_probabilities
      ~MCMTVChain.save_probabilities_dict
      ~MCMTVChain.save_stabilizer
      ~MCMTVChain.save_state
      ~MCMTVChain.save_statevector
      ~MCMTVChain.save_statevector_dict
      ~MCMTVChain.save_superop
      ~MCMTVChain.save_unitary
      ~MCMTVChain.sdg
      ~MCMTVChain.set_density_matrix
      ~MCMTVChain.set_matrix_product_state
      ~MCMTVChain.set_stabilizer
      ~MCMTVChain.set_statevector
      ~MCMTVChain.set_superop
      ~MCMTVChain.set_unitary
      ~MCMTVChain.size
      ~MCMTVChain.snapshot
      ~MCMTVChain.snapshot_density_matrix
      ~MCMTVChain.snapshot_expectation_value
      ~MCMTVChain.snapshot_probabilities
      ~MCMTVChain.snapshot_stabilizer
      ~MCMTVChain.snapshot_statevector
      ~MCMTVChain.squ
      ~MCMTVChain.swap
      ~MCMTVChain.sx
      ~MCMTVChain.sxdg
      ~MCMTVChain.t
      ~MCMTVChain.tdg
      ~MCMTVChain.tensor
      ~MCMTVChain.to_gate
      ~MCMTVChain.to_instruction
      ~MCMTVChain.toffoli
      ~MCMTVChain.u
      ~MCMTVChain.u1
      ~MCMTVChain.u2
      ~MCMTVChain.u3
      ~MCMTVChain.uc
      ~MCMTVChain.ucrx
      ~MCMTVChain.ucry
      ~MCMTVChain.ucrz
      ~MCMTVChain.unitary
      ~MCMTVChain.width
      ~MCMTVChain.x
      ~MCMTVChain.y
      ~MCMTVChain.z
   
   

   
   
   .. rubric:: Attributes

   .. autosummary::
   
      ~MCMTVChain.ancillas
      ~MCMTVChain.calibrations
      ~MCMTVChain.clbits
      ~MCMTVChain.data
      ~MCMTVChain.extension_lib
      ~MCMTVChain.global_phase
      ~MCMTVChain.header
      ~MCMTVChain.instances
      ~MCMTVChain.metadata
      ~MCMTVChain.num_ancilla_qubits
      ~MCMTVChain.num_ancillas
      ~MCMTVChain.num_clbits
      ~MCMTVChain.num_parameters
      ~MCMTVChain.num_qubits
      ~MCMTVChain.parameters
      ~MCMTVChain.prefix
      ~MCMTVChain.qubits
   
   
from qiskit import QuantumCircuit, execute, BasicAer

backend = BasicAer.get_backend('qasm_simulator')

qc = QuantumCircuit(5, 5)
qc.h(0)
qc.cx(0, range(1, 5))
qc.measure_all()

job = execute(qc, backend, shots=4321)
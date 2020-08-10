from qiskit.circuit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
repeated_qc = qc.repeat(3)
repeated_qc.decompose().draw(output='mpl')

from numpy import pi

from qiskit.circuit import EquivalenceLibrary
from qiskit.circuit import QuantumCircuit
from qiskit.circuit import QuantumRegister
from qiskit.circuit import Parameter
from qiskit.circuit.library import HGate
from qiskit.circuit.library import U2Gate
from qiskit.circuit.library import U3Gate

my_equiv_library = EquivalenceLibrary()

q = QuantumRegister(1, 'q')
def_h = QuantumCircuit(q)
def_h.append(U2Gate(0, pi), [q[0]], [])
my_equiv_library.add_equivalence(HGate(), def_h)

theta = Parameter('theta')
phi = Parameter('phi')
lam = Parameter('lam')
def_u2 = QuantumCircuit(q)
def_u2.append(U3Gate(pi / 2, phi, lam), [q[0]], [])
my_equiv_library.add_equivalence(U2Gate(phi, lam), def_u2)

my_equiv_library.draw()

from qiskit.circuit import QuantumCircuit

circ1 = QuantumCircuit(2)
circ2 = QuantumCircuit(2)

circ2.h(0)
circ1.cx(0, 1)

circ1.compose(circ2, front=True).draw(output='mpl')

from qiskit.circuit import QuantumCircuit

circuit_gate = QuantumCircuit(2)
circuit_gate.h(0)
circuit_gate.cx(0, 1)
custom_gate = circuit_gate.to_gate(label='My Special Bell')
new_circ = QuantumCircuit(2)
new_circ.append(custom_gate, [0, 1], [])
new_circ.draw(output='mpl')

from qiskit import QuantumCircuit
circuit = QuantumCircuit(2)
circuit.measure_all()
circuit.draw(output='mpl', cregbundle=True)

from qiskit import QuantumCircuit
circuit = QuantumCircuit(2)
circuit.measure_all()
circuit.draw(output='mpl', initial_state=True)

from qiskit import QuantumCircuit
from qiskit.circuit.library.standard_gates import YGate
circuit = QuantumCircuit(2)
circuit.append(YGate(label='A Y Gate').control(label='Y Control'), [0, 1])
circuit.draw(output='mpl')

from qiskit.circuit import QuantumCircuit

circ = QuantumCircuit(4)
circ.x(0)
circ.h(1)
circ.measure_all()
circ.draw(output='mpl')

from qiskit.circuit import QuantumCircuit

circ = QuantumCircuit(4)
circ.x(0)
circ.h(1)
circ.measure_all()
circ.draw(output='mpl', cregbundle=False)

from qiskit import QuantumCircuit
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.draw(output='mpl', scale=0.5)

from qiskit.circuit.library import XOR
import qiskit.tools.jupyter
circuit = XOR(5, seed=42)
%circuit_library_info circuit

from qiskit import execute
from qiskit import QuantumCircuit
from qiskit.providers.basicaer import BasicAer
from qiskit.visualization import plot_histogram

sim = BasicAer.get_backend('qasm_simulator')

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
result = execute([qc, qc, qc], sim).result()

plot_histogram(result.get_counts())

from qiskit import QuantumCircuit

circuit = QuantumCircuit(2)
circuit.measure_all()
circuit.draw(output='mpl', initial_state=True)

from qiskit.quantum_info import Statevector

state = Statevector.from_label('+0')
print(state.to_dict())

from qiskit.quantum_info import DensityMatrix

state = DensityMatrix.from_label('+0')
print(state.to_dict())

from qiskit.quantum_info import Statevector

state = Statevector.from_label('+0')
print(state.probabilities())

from qiskit.quantum_info import DensityMatrix

state = DensityMatrix.from_label('+0')
print(state.probabilities())

from qiskit.quantum_info import Statevector

state = Statevector.from_label('+0')
print(state.probabilities_dict())

from qiskit.quantum_info import DensityMatrix

state = DensityMatrix.from_label('+0')
print(state.probabilities_dict())

from qiskit.quantum_info import Statevector

psi = Statevector.from_label('+0')
shots = 1024

# Sample counts dictionary
counts = psi.sample_counts(shots)
print('Measure both:', counts)

# Qubit-0
counts0 = psi.sample_counts(shots, [0])
print('Measure Qubit-0:', counts0)

# Qubit-1
counts1 = psi.sample_counts(shots, [1])
print('Measure Qubit-1:', counts1)

from qiskit.quantum_info import Statevector

psi = Statevector.from_label('-1')
shots = 10

# Sample memory
mem = psi.sample_memory(shots)
print('Measure both:', mem)

# Qubit-0
mem0 = psi.sample_memory(shots, [0])
print('Measure Qubit-0:', mem0)

# Qubit-1
mem1 = psi.sample_memory(shots, [1])
print('Measure Qubit-1:', mem1)

from qiskit.quantum_info import Statevector

psi = Statevector.from_label('+1')

# Measure both qubits
outcome, psi_meas = psi.measure()
print("measure([0, 1]) outcome:", outcome, "Post-measurement state:")
print(psi_meas)

# Measure qubit-1 only
outcome, psi_meas = psi.measure([1])
print("measure([1]) outcome:", outcome, "Post-measurement state:")
print(psi_meas)

from qiskit.quantum_info import Statevector

psi = Statevector.from_label('+1')

# Reset both qubits
psi_reset = psi.reset()
print("Post reset state: ")
print(psi_reset)

# Reset qubit-1 only
psi_reset = psi.reset([1])
print("Post reset([1]) state: ")
print(psi_reset)

from qiskit.visualization import visualize_transition
from qiskit import *

qc = QuantumCircuit(1)
qc.h(0)
qc.ry(70,0)
qc.rx(90,0)
qc.rz(120,0)

visualize_transition(qc, fpg=20, spg=1, trace=True)

from qiskit import QuantumCircuit

circuit = QuantumCircuit(2)
circuit.measure_all()
circuit.draw(output='text')

from qiskit import QuantumCircuit

circuit = QuantumCircuit(2)
circuit.measure_all()
circuit.draw(output='text', initial_state=True)

from qiskit.transpiler import CouplingMap

coupling_map = CouplingMap(
    [[0, 1], [1, 0], [1, 2], [1, 3], [2, 1], [3, 1], [3, 4], [4, 3]])
coupling_map.draw()

from qiskit.transpiler import CouplingMap

coupling_map = CouplingMap.from_line(5)
coupling_map.draw()

from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.test.mock import FakeVigo

qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
transpiled_qc = transpile(qc, FakeVigo())
transpiled_qc.draw(output='mpl')

from qiskit.pulse import *
from qiskit.pulse import library as pulse_lib

gp0 = pulse_lib.gaussian(duration=20, amp=1.0, sigma=1.0)
sched = Schedule()
channel_a = DriveChannel(0)
channel_b = DriveChannel(1)
sched += Play(gp0, channel_a)
sched = sched.insert(60, ShiftPhase(-1.57, channel_a))
sched = sched.insert(30, ShiftPhase(-1.50, channel_b))
sched = sched.insert(70, ShiftPhase(1.50, channel_b))

sched.draw(show_framechange_channels=False)
from qiskit import QuantumCircuit, Aer, transpile, assemble
import cirq
import numpy as np

class SuperQubit:
    def __init__(self, num_qubits=1):
        # Initialisation avec un nombre variable de qubits
        self.qubits = cirq.LineQubit.range(num_qubits)
        self.circuit = cirq.Circuit()
        self.state = None

    def apply_super_hadamard(self):
        """
        Applique une porte Hadamard sur tous les qubits.
        """
        self.circuit.append(cirq.H.on_each(*self.qubits))

    def apply_real_quantum_gate(self, angle):
        """
        Applique une porte quantique réelle (Ry) sur tous les qubits avec un angle spécifié.
        """
        self.circuit.append(cirq.ry(angle).on_each(*self.qubits))

    def measure(self, repetitions=1):
        """
        Effectue une mesure du circuit quantique.
        """
        self.circuit.append(cirq.measure(*self.qubits, key='result'))

        # Simulation du circuit
        simulator = cirq.Simulator()
        results = simulator.run(self.circuit, repetitions=repetitions)

        # Obtention des résultats de la mesure
        self.state = results.measurements['result']

    def get_state(self):
        return self.state

# Utilisation de la classe SuperQubit avec Cirq
num_qubits = 3  # Par exemple, 3 qubits
super_qubit = SuperQubit(num_qubits)
super_qubit.apply_super_hadamard()
super_qubit.apply_real_quantum_gate(np.pi/4)  # Angle de rotation de pi/4
super_qubit.measure(repetitions=1000)
results = super_qubit.get_state()

print("Results of measurements:", results)

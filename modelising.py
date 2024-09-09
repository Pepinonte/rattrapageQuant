from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
import numpy as np

# Créer un registre quantique avec 2 qubits
qreg = QuantumRegister(2, 'q')

# Créer un registre classique avec 2 bits
creg2 = ClassicalRegister(2, 'c')

# Créer un circuit quantique en utilisant les registres
qcircuit = QuantumCircuit(qreg, creg2)

#----------------------------------------------------------

# Application de la porte Hadamard au premier qubit (qubit 0)
qcircuit.h(0)

# Application de la porte Hadamard au deuxième qubit (qubit 1)
qcircuit.h(1)

#----------------------------------------------------------

# Application de la porte CNOT avec le qubit 0 comme contrôle et le qubit 1 comme cible
qcircuit.cx(0, 1)

#----------------------------------------------------------

# Application des rotations Rz
theta = np.pi / 4  # Exemple d'angle (45 degrés)
qcircuit.rz(theta, 0)  # Rotation autour de l'axe z pour le qubit 0
qcircuit.rz(theta, 1)  # Rotation autour de l'axe z pour le qubit 1

#----------------------------------------------------------

# Mesurer les qubits et stocker les résultats dans les bits classiques
qc.measure([0, 1], [0, 1])

# Affichage du circuit
print(qc)
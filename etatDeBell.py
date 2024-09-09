from qiskit import QuantumCircuit,QuantumRegister, QuantumCircuit, ClassicalRegister, execute, Aer

# # Création du circuit quantique avec 2 qubits et 2 bits classiques
# qc = QuantumCircuit(2, 2)

# Créer un registre quantique avec 2 qubits
qreg = QuantumRegister(2, 'q')

# Créer un registre classique avec 2 bits
creg2 = ClassicalRegister(2, 'c')

# Créer un circuit quantique en utilisant les registres
qc = QuantumCircuit(qreg, creg2)

#----------------------------------------------------------

# Application de la porte Hadamard au premier qubit (qubit 0)
qc.h(0)

#----------------------------------------------------------

qc.cx(0, 1)

#----------------------------------------------------------

# Mesurer les qubits et stocker les résultats dans les bits classiques
qc.measure([0, 1], [0, 1])

# Affichage du circuit
print(qc)

# Exécution du circuit sur un simulateur
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()

# Récupération des résultats
counts = result.get_counts(qc)
print("Résultats de la mesure :", counts)
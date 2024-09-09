# Importation des bibliothèques nécessaires
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

# Créer un registre quantique avec 2 qubits
qreg = QuantumRegister(2, 'q')

#----------------------------------------------------------

# Créer un registre classique avec 2 bits
creg2 = ClassicalRegister(2, 'c')

#----------------------------------------------------------

# Créer un circuit quantique en utilisant ce registre
qcircuit = QuantumCircuit(qreg, creg2)

# Optionnel : Visualiser le circuit (vide pour l'instant)
qcircuit.draw(output='mpl')

#----------------------------------------------------------

# Ajouter une porte Hadamard au premier qubit (q0)
qcircuit.h(qreg[0])

# Ajouter une porte CNOT entre le premier qubit et le second (q1)
qcircuit.cx(qreg[0], qreg[1])

# Afficher le circuit avec les opérations
qcircuit.draw(output='mpl')

#----------------------------------------------------------

# Appliquer une porte Z sur l'état |01⟩ (contrôle sur le second qubit)
qcircuit.cz(qreg[1], qreg[0])

# Appliquer une porte X sur l'état |10⟩ (contrôle sur le premier qubit)
qcircuit.cx(qreg[0], qreg[1])

# Appliquer des portes X et Z sur l'état |11⟩
qcircuit.cx(qreg[1], qreg[0])  # Porte X contrôlée
qcircuit.cz(qreg[1], qreg[0])  # Porte Z contrôlée

#----------------------------------------------------------

# Appliquer une porte CNOT avec le premier qubit (q0) comme contrôle et le second qubit (q1) comme cible
qcircuit.cx(qreg[0], qreg[1])


#----------------------------------------------------------

# Appliquer une porte Hadamard au premier qubit (q0)
qcircuit.h(qreg[0])

# Appliquer une porte Hadamard au premier qubit (q0) pour créer une superposition
qcircuit.h(qreg[0])

# Mesurer les qubits et stocker les résultats dans les registres classiques
qcircuit.measure(qreg, creg2)

#----------------------------------------------------------

# Configurer le simulateur quantique
simulator = Aer.get_backend('qasm_simulator')

# Exécuter le circuit sur le simulateur
job = execute(qcircuit, simulator, shots=1024)

# Obtenir les résultats
result = job.result()

# Extraire les comptes des résultats
counts = result.get_counts(qcircuit)

# Afficher les résultats
print(counts)
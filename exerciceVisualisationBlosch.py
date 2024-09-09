from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
import numpy as np

# Créer un registre quantique avec 2 qubits
qreg = QuantumRegister(1, 1)

# Créer un circuit quantique en utilisant ce registre
qcircuit = QuantumCircuit(qreg)

#----------------------------------------------------------

def prepare_arbitrary_state(a, b):
    """
    Prépare l'état quantique |ψ⟩ = a|0⟩ + b|1⟩ en utilisant les rotations appropriées.
    
    Arguments:
    a -- Coefficient complexe pour |0⟩
    b -- Coefficient complexe pour |1⟩
    
    Retourne:
    qc -- Circuit quantique préparant l'état |ψ⟩
    """
    # Normaliser les coefficients a et b
    norm = np.sqrt(np.abs(a)**2 + np.abs(b)**2)
    a /= norm
    b /= norm
    
    # Calculer les angles nécessaires pour les rotations
    theta = 2 * np.arccos(np.abs(a))
    phi = np.angle(b) - np.angle(a)
    
    # Créer le circuit quantique avec 1 qubit
    qc = QuantumCircuit(1)
    
    # Appliquer la rotation autour de l'axe y par l'angle theta
    qc.ry(theta, 0)
    
    # Appliquer la rotation autour de l'axe z par l'angle phi
    qc.rz(phi, 0)
    
    return qc

# Exemple d'utilisation de la fonction
a = np.exp(1j * np.pi / 4) / np.sqrt(2)  # Coefficient pour |0⟩
b = np.exp(1j * np.pi / 4) / np.sqrt(2)  # Coefficient pour |1⟩
qc = prepare_arbitrary_state(a, b)
print(qc)
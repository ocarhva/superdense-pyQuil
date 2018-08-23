import math
import numpy as np

from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import H, X, Z, CNOT

qvm = QVMConnection()


def transformacionDeAlice(mensajeDeAlice):
    
    #Entrelazamiento de los qubits
    program = estadoDeBell()
    
    #Alice aplica la compuerta apropiada
    if (mensajeDeAlice == "11"):
        program += Program(X(0), Z(0))

    elif (mensajeDeAlice == "01"):
        program += Program(X(0))

    elif (mensajeDeAlice == "10"):
        program += Program(Z(0))

    return program

#Entrelazo los qubits de Alice y Bob
def estadoDeBell():
    
    program = Program()
    program.inst((H(0)), CNOT(0,1))

    return program

def lecturaDeBob(program):
    program += Program(CNOT(0,1), H(0))

    read_message = program.measure_all()

    result = qvm.run(read_message)

    print("Mensaje recibido por Bob:", result[0][0], result[0][1])



mensajeDeAlice = input("Mensaje de Alice (Dos bits clasicos): ")

program = transformacionDeAlice(mensajeDeAlice)

lecturaDeBob(program)

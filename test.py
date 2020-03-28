from sympy import prime
prime(0)

# from qiskit.aqua.algorithms import Shor
# from qiskit.aqua import QuantumInstance
# from qiskit import Aer
#
# from qiskit.providers.aer import QasmSimulator
# # class shor(a,N)
# # N(int) – The integer to be factored
# # a – random integer that satisfies a < N and gcd(a, N) = 1
# backend = QasmSimulator()
# #Aer.get_backend("qasm_simulator")
# # for backend in Aer.backends():
# #      print(backend.name())
#
# shor = Shor(31, 3)
# qu_inst = QuantumInstance(backend=backend, shots=1024, seed_simulator=1, seed_transpiler=1)
# print(shor.run(qu_inst))

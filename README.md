# variational_quantum_state_tomography

Variational methods have a wide range of application in optimization and machine learning. However, they can also be used to study quantum computers. Currently, we are in an era where quantum computers present a large amount of noise due to the low number of qubits (<100) and the low fidelity of the gates. In this era, known as the noisy intermediate-scale quantum (NISQ), characterizing how quantum devices work is critical. One way to achieve this is through [quantum tomography](https://en.wikipedia.org/wiki/Quantum_tomography). This consists of protocols that allow obtaining the quantum state of a system, which can be a prior unknown. In this notebook we will implement a variational tomographic method for pure quantum states, based on https://arxiv.org/abs/1406.4101. 

This is a tutorial of the method for the method using as a benchmark a GHZ state: [Variational Quantum State Tomography](./Variational_Quantum_Tomography.ipynb)

One of the highlights of variational tomography is its applications for high-dimentional Hilbert spaces. If the have a parametrization of the state, for example, as a [MPS](https://en.wikipedia.org/wiki/Matrix_product_state), we can apply the method successfully, as we show [here](./Variational_Quantum_Tomography_26qb.ipynb) and [here](./Variational_Quantum_Tomography_30qb.ipynb)


![Bloch](https://github.com/lezav/variational_quantum_state_tomography/blob/main/Bloch%20Sphere/b1.png)


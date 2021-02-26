# Variational Quantum State Tomography

Variational methods have a wide range of application in optimization and machine learning. However, they can also be used to study quantum computers. Currently, we are in an era where quantum computers present a large amount of noise due to the low number of qubits (<100) and the low fidelity of the gates. In this era, known as the noisy intermediate-scale quantum (NISQ), characterizing how quantum devices work is critical. One way to achieve this is through [quantum tomography](https://en.wikipedia.org/wiki/Quantum_tomography). This consists of protocols that allow obtaining the quantum state of a physical system, which can be a prior unknown. In this work we will implement a variational tomographic method for pure quantum states, based on this [paper](https://arxiv.org/abs/1406.4101) of Christopher Ferrie. 

This is a tutorial of the method using as a benchmark a GHZ state: [Variational Quantum State Tomography](./Presentation.ipynb)

One of the highlights of variational tomography is its applications for high-dimentional Hilbert spaces. If the have a parametrization of the state, for example, as a [MPS](https://en.wikipedia.org/wiki/Matrix_product_state), we can apply the method successfully, as we show [here](./Variational_Quantum_Tomography_26qb.ipynb) for 26 qubits and [here](./Variational_Quantum_Tomography_30qb.ipynb) for 30 qubits. 
 
Finally, in the following figure we observe the evolution of the algorithm as a function of the number of iterations: as *k* increases, our initial guess state | 0 > state approaches the state of the system | 1 >. 
<p align="center">
  <img width="380" height="380" src="https://github.com/lezav/variational_quantum_state_tomography/blob/main/Qubit_example/b1.png">
</p>


Further reading 

https://en.wikipedia.org/wiki/Quantum_tomography. The article on wikipedia for quantum tomography. 

http://research.physics.illinois.edu/QI/Photonics/tomography-files/tomo_chapter_2004.pdf. Here are some theoretical and experimental foundations for standard quantum tomography on photonics systems.

https://arxiv.org/abs/1608.02263. This is a experimental realization of quantum tomography for 7 qubits using compressed sensing, a type of quantum tomography. It shows the difficulties of estimating quantum states for an increasing number of qubits. 

https://arxiv.org/abs/1406.4101. Quantum tomography using SPSA.

https://www.nature.com/articles/s41598-019-52289-0. An improvement on the previous paper with a parametrization in the complex numbers. 

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pennylane as qml    
from pennylane import numpy as np    


# In[2]:


class SPSA:
    """
    Simultaneous perturbation stochastic approximation optimization method
    """
    
    def __init__( self, a=3 , c=0.01, A=0, α=0.602 , γ=0.101):
        self._a = a
        self._c = c
        self._A = A
        self._α = α
        self._γ = γ
        
    def step( self, function, θ, k ):
        
        ak = self._a/(k+self._A+1)**self._α, 
        ck = self._c/(k+1)**self._γ
                
        Δ  = 2*np.round( np.random.rand(θ.size).reshape(θ.shape) )-1
        
        θ_plus  = θ + ck*Δ
        θ_minus = θ - ck*Δ   
        
        function_plus  = function( θ_plus )  
        function_minus = function( θ_minus )  
        
        ghat = np.divide( function_plus-function_minus, 2*ck*Δ + 1e-8 )
        
        return θ - ak*ghat 


# In[ ]:


def VQT( circuit_state, circuit_variational, parameters, max_iterations, device, optimizator=SPSA() ):
    """
    Variational Quantum Tomography
    """
    @qml.qnode(device)
    def Fidelity(params):
        n_wires = device.num_wires
        circuit_state( n_wires )
        circuit_variational(params, n_wires)
        return qml.probs(wires=range(n_wires))
    
    infidelities   = []
    parameters_out = []
    objective      = lambda params : 1 - Fidelity(params)[0]
    
    for n in range(max_iterations):
        parameters = optimizator.step( objective, parameters, n )
        infidelities.append( objective(parameters) )
        parameters_out.append(parameters)
    
    return parameters_out, infidelities


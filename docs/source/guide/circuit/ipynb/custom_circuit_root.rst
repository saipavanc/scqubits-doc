Custom Circuits
===============

The ``Circuit`` class provides functionality for the symbolic and
numerical analysis of custom circuits.

For a custom circuit, the code

- **identifies the periodic and extended degrees of freedom**,
- **eliminates the free and frozen modes**.

With this, the symbolic expression of the Hamiltonian is generated in
terms of an appropriate choice of variables. The ``Circuit`` class also
performs the numerical diagonalization of the circuit Hamiltonian.
Hierarchical diagonalization can be enabled for better runtime/memory
perfomance.

.. image:: ./circuit-flowchart.png
  :width: 400

.. toctree::
   :maxdepth: 1

   custom_circuit_define.ipynb
   custom_circuit_define_more.ipynb
   custom_circuit_lagrangian.ipynb
   custom_circuit_hamiltonian.ipynb
   custom_circuit_bases.ipynb
   custom_circuit_hd.ipynb
   custom_circuit_visualization.ipynb
   custom_circuit_offsets.ipynb
   custom_circuit_coherence_estimates.ipynb
   custom_circuit_parametric_driving.ipynb
   custom_circuit_extra.ipynb

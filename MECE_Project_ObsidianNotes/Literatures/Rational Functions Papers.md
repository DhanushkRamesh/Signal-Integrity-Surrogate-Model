- Parametric Modeling of Microwave Components Using Adjoint Neural Networks and Pole-Residue Transfer Functions With EM Sensitivity Analysis 

Referred this paper to establish the mathematical framework to maintain physical continuity in high-dimensional design.

Here the core objective is the sensitivity analysis based neuro transfer function that utilizes the EM sensitivity information to increase the model accuracy and also to reduce the aount of data required for training.

They use a dual model structure
- Original Neuro Transfer Function: This function maps the geometrical parameters to s-parameters.
- Adjoint Neuro Transfer Function: This model maps the same parameters to the derivatives of the responses.

This model uses pole-residue format - Instead of treating the s-parameters as arbitrary function, it defines a function as a function of frequency using poles and residues.

Here they use advanced pole-residue tracking method, The order (no. of poles) can change as the geometry shifts. This causes mathematical discontinuity  this is one of the challenge in SI modeling. 

They use pole splitting and sensitivity guided selection. 
Pole Splitting: When the geometry needs more poles than its neighbors, the algorithm splits one existing poles into two overlapping poles.

Sensitivity Guided Selection: In order to maintain a smooth and continuous pole movement, the model uses derivative information to mathematically determine which pole is splitting apart.

The model employs a two-stage training process. There is a priliminary training on the extracted poles and residue data followed by model refinement against the final EM response. This helps with data efficiency and accuracy.

- Rational neural networks

This papaer stands as the proof for why using a Rational Neural Network is superior over a standard ReLU network. 

This says rational layers are resourceful while capturing the sharp resonances and dips.

Using a tye (3, 2) rational function ( A degree 3 numerator and degree 2 denominator) - it allows the function to behave like a non-constant linear functions whihc is more flexible.

Rational Neural Net provide better initialization - where the initialization will be the best rational approximation of the ReLU function. This ensure that the training start form  a well-understood baseline instead of the network learning its own optimal shape.


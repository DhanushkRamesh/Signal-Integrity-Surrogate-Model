High-Speed digital circuits are prone and sensitive to physical defects resulting in degradation of signal integrity as the data rate increases. This is because of non-ideal effects like skin effect and surface roughness.

High-speed digital design requires yield analysis - that need a vast amount of simulations (manufacturing variations/Tolerances) to ensure the circuit won't fail in mass production. Currently there are a few methods used in the industry,
- Commercial Solvers (HFSS/CST): These commercial solvers are of high accuracy but they are very slow for generating 10,000 + simulations which may take months to simulate.
- Standard AI innovations: AI models are being adapted to make the simulation faster but most of them use basic models, and recent innovations of using complex models have unconstrained approximations which may fail while there is a slight variation during the manufacturing.
- There are very few physics-informed models usually with soft physical constraints which are mostly not architectural.
- There are quite a few established forward model to predict the s-parameters from the given input geometrics but the exploration on a proper inverse design process is less. In this project we try to explore the inverse model to predict the geometrics from the target s-parameters also considering the manufacturing yield.

Problem Statement: There are a lot of well established forward models that area explored in SI applications where the s-parameters are predicted from the given input geometry. But, the inverse design models are still not very much explored to find the desired geometrics form the target s-parameter. We also try to solve the one-to-many problem where one target s-parameter can have many design options.

**Research Question**: 

How can we construct a physics-constrained inverse framework to not only solve the non-uniqueness of electromagnetic scattering, but also make sure it is robust while manufacturing and guarantee physical causality under sparse data regime?

Solution: Tandem VAE architecture (focusing on physics and yield)

We try to solve the non-uniqueness also by ensuring the causality and passivity integrated in the architecture so the model is physics-informed and hard constrained. The proposal will be a Yield-Tandem VAE (Variational Autoencoder) focusing on the yield where we keep (+10% or -10% while manufacturing)

We plan a Tandem networks where there is a forward and inverse network coupled together (arranged in Tandem conf)

- **Forward Model**: This acts as a physics proxy which act as a pre-trained surrogate that maps the input geometrics to S-Parameters. We use Rational function layer in this model to enforce physical constraints (in the architecture)

- **Inverse Model**: This will be a conditional VAE (variational autoencoder) that maps the target s-parameter to the valid geometrics.

We Train the model with a physics-informed loop where the inverse model proposed a geometry which will be passed through the forward surrogate through the frozen proxy. The errors are calculated in the S-parameter domain and variables are then back propagated to the inverse model through the proxy.

**Forward Model** (Proxy) - (got this idea while i was exploring SciML) - need your validation if it is okay to proceed with it? and if its a good idea to implement in first place. 

- We model this by introducing a Differential Rational Function Layer. Instead of predicting the raw magnitude or phase, the forward model predicts the coefficients  of a Rational Transfer function  in the pole-residue form. 

- We enfrce causality and passivity via a modified softplus activation where the real part of every pole must be less than 0 (strictly negative). Also, to ensure the time-domain impulse response in real valued, we generate poles in complex conjugate pairs. 

**Inverse Model** (Generator)

We address the one-to many problem by employing Conditional VAE which introduces a stochastic latent variable that captures multimodal nature of the design. 
	- The encoder maps the geometrics to a latent distribution
	- Decoder samples the latent distribution and conditions on the target to reconstruct the geometry. 
we can get multiple valid design options through this.

**Jacobian Yield Optimization** - (I was exploring similar noise toleration problem and Computer Vision applications looked similar)

We integrate manufacturing yield directly into the loss function. So we try to define a robust design whose performance in invariant to small manufacturing issues. Jacobian Regularization is inspired in this project from many computer vison applications, here we use it to minimizing the sensitivity of the s-parameters wrt the geometry. Through this we can find the flat minima in the optimization landscape.

Unsupervised Learning Layer:

We also plan to implement and active learning loop to mitigate the high computational cost of ground truth simulations. We plan to use openEMS here.

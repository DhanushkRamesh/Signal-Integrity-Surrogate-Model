
## On-Demand Inverse Design for Narrowband Nanophotonic Structures Based on Generative Model and Tandem Network

This paper is the the foundational inspiration to use conditional Variational Autoencoders (cVAE) along with Tandem Network.

This paper uses a two-stage hybrid arch. 
1. cVAE - The cVAE  translates the sparce Ideal Target Spectra (ITS) into a cVAE adjusted target spectrum instead of predicting the structure directly. 
2.  Tandem Network: The CTS is fed to the inverse model which then predicts the structural parameters. This is then fed to the pre-trained forward model for validation.
Results prove that the use of cVAE component stabilizes the inverse mappinp with reliable initial spectral priors.

## Leveraging generative neural networks for accurate, diverse, and robust nanoparticle design

In this paper they research the use of Variational Autoencoderto generate multiple, diverse, accurate results. They compare the use of VAE with Tandem Network - to address one-to-many mapping problem.

Architecture:

The VAE architecture - Encoder: Takes the paartical design and optical condition to map to low-dimensional latent space.

Decoder: Uses the latent vector and the condition to reconstruct the design parameters. 

They used AdamW optimizer to improve training speed and maintain accuracy.

In the results - VAE was superior as it could explore the latent space to ind several different structures that met the same target spectra.




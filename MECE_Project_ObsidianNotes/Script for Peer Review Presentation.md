
Slide 1: The Hook

Image idea: 

Imagine building a F1 car that breaks if the wind changes by 1 mile per hour. This is the case in the high-speed circuit design today.

As we are moving to 112G data rates, the electrical signals are so sensitive that a microscopic error while manufacturing - say a drill bit going 10% deep, can destroy the signal integrity of the PCB.

The problem is most of the current state-of -the-art AI models focus only on accuracy finding single optimal design point. These work perfectly in computer simulations but fails when it hits the factory floor even if there is minor tolerances. While the industry has mastered the forward simulation, robust inverse design remains largely unsolved. 

My project challenges this by asking: _Can we build an AI that doesn't just design for 'Performance', but designs for 'Manufacturability' and 'Physics'?_"

Slide 2:  Proposed Solution

We propose a novel framework - the yield focused Tandem-VAE network that moves beyond standard Deep Learning by integrating three specific innovations,

First, to solve the one-to-many problem - where multiple geometries can produce the same signal. We use conditional Variational Autoencoders (cVAE) - unlike standard regression model that output a single average design, we generate a distribution of valid geometries for the engineers to choose from. 

Second, to enforce physics. We introduce a Differentiable Rational Layer, replacing the computationally heavy complex penalty functions to enforce physics (causality). Our network predicts poles and residues, instead of raw data points. This mathematically guarantees that every generated design obeys Kramers-Kronig causality, hence preventing the AI from hallucinating. 

Third, and most importantly, we are introducing a Jacobian Yield Loss, inspired from Scientific Machine Learning, and also mostly used in Computer Vision applications. We use a Finite-difference approximation of the Jacobian matrix during training. This penalizes the designs that are sharp peaks where a small change leads to failure - and forces the model to find flat plateaus that is stable even with some manufacturing tolerances.

Slide 3: Why it matters

Why does this matter? Because in hardware industry, Yield is the King!

The design that works in simulation and fails in the factory cost millions in re-spins. Also, most of the standard inverse papers ignore yield.  Our work bridges the gap between academic AI and industrial reality.

By optimizing the Jacobian, we guarantee that the designs will be robust and by enforcing rational layer the engineers know that the AI isn't violating physics. 

This ultimately moves from using AI as a simple calculator to using it as a physics aware co-designer that can accelerate the design development from weeks of simulation to milliseconds of interface.


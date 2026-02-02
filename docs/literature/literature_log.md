**Literature Search Log**

**Student:** Dhanush Kumar Ramesh

**Supervisor:** Dr. Marissa Condon

**Project:** ML-Based Surrogate Model For Signal Integrity


| Date | Database | Search Terms | Results | Useful Hits |
| :--- | :--- | :--- | :--- | :--- |
| 30-11-2025 | IEEE Xplore | "integrated circuit modelling" AND "signal Integrity applications" AND "Neural Networks" | 27 | 1 (Akinwande et al.) |
| 03-12-2025 | IEEE Xplore | "high-density interconnects" AND "machine learning" | 43 | 1 (Sreekumar & Gupta) |
| 07-01-2026 | Google Scholar | "physics-informed" AND "interconnects" | 1600 | 3 (Garbuglia et al.) (J. Fan et al) (T. -L. Wu et al.) |


## 2. Log of Articles Reviewed


### 1. Core reference paper
**Citation:**
O. Akinwande, S. Erdogan, R. Kumar and M. Swaminathan, "Surrogate Modeling With Complex-Valued Neural Nets for Signal Integrity Applications," in IEEE Transactions on Microwave Theory and Techniques, vol. 72, no. 1, pp. 478-489, Jan. 2024, doi: 10.1109/TMTT.2023.3319835. 
**Key Findings:**
* Proposes the complex-valued Neural Networks method to handle the phase information in machine learning  which is the core idea to develop our forward and inverse model. 
**Relevance**
* This is the primary reference for our forward model.

### 2. High-Density Interconnects
**Citation:**
D. Sreekumar and S. Gupta, "Efficient Synthesis and Simulation of High-Density Interconnects Using Machine Learning," 2025 IEEE 29th Workshop on Signal and Power Integrity (SPI),Gaeta, Italy, 2025, pp. 1-4, doi: 10.1109/SPI64682.2025.11014451. 

**Key Findings:**
*Discussed the sysnthesis of interconnects using machine learning which can be very usefull for data generation.
**Relevance**
it offers insights on simulation strategy for data generation of high-density designs.

**Key Findings:**
### 3. Physics-Informed Modeling
**Citation:**
F. Garbuglia, T. Reuschel, C. Schuster, D. Deschrijver, T. Dhaene and D. Spina, "Modeling Electrically Long Interconnects Using Physics-Informed Delayed Gaussian Processes," in IEEE Transactions on Electromagnetic Compatibility, vol. 65, no. 6, pp. 1715-1723, Dec. 2023, doi: 10.1109/TEMC.2023.3317917. 

**Key Findings:**
This paper used Guassian process which gives insights on physivs informed loss-functions that we refer for model design to make it accurate not just for the exact values but also for the range of values while predicting the output params.

**Relevance:**
* It is useful for considering how the moedel need to be modified and designed on combining physics informed loss and complex valued neural network.

### 4. SI Fundamentals
**Citation:**
J. Fan, X. Ye, J. Kim, B. Archambeault and A. Orlandi, "Signal Integrity Design for HighSpeed Digital Circuits: Progress and Directions," in IEEE Transactions on Electromagnetic Compatibility, vol. 52, no. 2, pp. 392-400, May 2010, doi: 10.1109/TEMC.2010.2045381.

**Relevance** 
* This paper is used to find the problem statement that we are solving which gives foundational knoledge on the non-ideal effects (skin-effects and surface roughness)

### 5. PCB Technology Overview
**Citation:**
T. -L. Wu, F. Buesink and F. Canavero, "Overview of Signal Integrity and EMC Design Technologies on PCB: Fundamentals and Latest Progress," in IEEE Transactions on Electromagnetic Compatibility, vol. 55, no. 4, pp. 624-638, Aug. 2013, doi: 10.1109/TEMC.2013.2257796. 

**Relevance**
* This paper gives the context for stochastic manufacturing variations during the manufacture of PCB. This will help us with the project to consider the schotastic variation while predicting the s-params and during the output.


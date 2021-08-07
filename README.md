# NLMS-Malaria

### Intro
Repository of fitting algorithms for nonlinear functions related to Malaria Treatment.


Concentration data from tests of two drugs A and B, and the respective velocity of action from drug A  compiled into a CSV File.
This repo uses Scipy's `curve-fit` function to fit the model parameters to the data using Non-Linear Mean Squares.

### First Test: Hyperbolic Mixed-type Inhibition Model
![Hyperbolic Mixed-type Inhibition Model](imgs/Modelo.jpg?raw=true "Hyperbolic Mixed-type Inhibition Model")

The original test involves the Hyperbolic Mixed-type Inhibition Model calculating the parameters for:
 - Vmax
 - Alpha
 - Beta
 - Ks1
 - Ks2


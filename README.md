# 1. What is the quasi-harmonic approximation ?

Since the birth of quantum chemistry, almost every calculation was performed in the athermal limit (0K) and no pressure effects were considered (0Pa).
One of the most exciting challenges in an _ab intio_ calculation is to obtain information of the system at a finite temperature and pressure. This allow us to obtain a more realistic picture of the system in the everyday world, where temperature and pressure cannot be neglected and are indeed the driving force for many transformations in nature.

One of the most famous techniques for taking into account the effect of the temperature in the computed properties of molecules and crystals is _ab intio_ molecular dynamics [], in which the Schrodinger equation is solved at each MD time step within the Born-Oppenheimer approximation. Unfortunetely, this is a very computationally expensive technique. Therefore, there is a huge interest in developing accurate and reliable models for the inclusion of the temperature in the standard first-principles quantum chemical methods.

The quasi-harmonic approximation is an elegant way to tacke with this problem in condensed matter, by considering each atom as an independent harmonic oscillator:

![Data flow](https://github.com/DavidCdeB/QHA/blob/master/levels_vibrat_cropped.png)

For a given independent harmonic oscillator, by summing over all these levels it is possible to derive the partition function:


<a href="https://www.codecogs.com/eqnedit.php?latex=Z_{i,&space;\mathbf{k}}&space;=&space;\frac{\exp\left&space;(&space;-\frac{h\nu_{i}\left&space;(&space;\mathbf{k}&space;\right&space;)}{2k_{B}T}&space;\right&space;)}{1-\exp\left&space;(&space;-\frac{h\nu_{i}\left&space;(&space;\mathbf{k}&space;\right&space;)}{k_{B}T}&space;\right&space;)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_{i,&space;\mathbf{k}}&space;=&space;\frac{\exp\left&space;(&space;-\frac{h\nu_{i}\left&space;(&space;\mathbf{k}&space;\right&space;)}{2k_{B}T}&space;\right&space;)}{1-\exp\left&space;(&space;-\frac{h\nu_{i}\left&space;(&space;\mathbf{k}&space;\right&space;)}{k_{B}T}&space;\right&space;)}" title="Z_{i, \mathbf{k}} = \frac{\exp\left ( -\frac{h\nu_{i}\left ( \mathbf{k} \right )}{2k_{B}T} \right )}{1-\exp\left ( -\frac{h\nu_{i}\left ( \mathbf{k} \right )}{k_{B}T} \right )}" /></a>

where there is a value of frequency for each **k** vector. In a molecule, this is equivalent to a unique value of *k* (the Gamma point).

It is not difficult to derive the Helmholtz free energy, entropy and Gibbs free energy:


<a href="https://www.codecogs.com/eqnedit.php?latex=F&space;=&space;U&space;&plus;&space;\frac{1}{2}\sum_{i,\mathbf{k}}&space;h\nu_{i}&space;\left&space;(&space;\mathbf{k}&space;\right&space;)&space;&plus;&space;k_{B}&space;T&space;\sum_{i,&space;\mathbf{k}}&space;\ln&space;\left&space;[&space;1-\exp&space;\left&space;(&space;\frac{-h\nu_{i}&space;\left&space;(&space;\mathbf{k}&space;\right&space;)&space;}{k_{B}T}&space;\right&space;)&space;\right&space;]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F&space;=&space;U&space;&plus;&space;\frac{1}{2}\sum_{i,\mathbf{k}}&space;h\nu_{i}&space;\left&space;(&space;\mathbf{k}&space;\right&space;)&space;&plus;&space;k_{B}&space;T&space;\sum_{i,&space;\mathbf{k}}&space;\ln&space;\left&space;[&space;1-\exp&space;\left&space;(&space;\frac{-h\nu_{i}&space;\left&space;(&space;\mathbf{k}&space;\right&space;)&space;}{k_{B}T}&space;\right&space;)&space;\right&space;]" title="F = U + \frac{1}{2}\sum_{i,\mathbf{k}} h\nu_{i} \left ( \mathbf{k} \right ) + k_{B} T \sum_{i, \mathbf{k}} \ln \left [ 1-\exp \left ( \frac{-h\nu_{i} \left ( \mathbf{k} \right ) }{k_{B}T} \right ) \right ]" /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=S&space;=&space;-k_{B}&space;\sum_{i,&space;\mathbf{k}}\ln&space;\left&space;[&space;1-\exp\left&space;(&space;\frac{-h\nu_{i}&space;\left&space;(\mathbf{k}\right&space;)&space;}{k_{B}T}&space;\right&space;)&space;\right&space;]&space;&plus;&space;\frac{h}{T}&space;\sum_{i,&space;\mathbf{k}}\,\frac{\nu_{i}&space;\left&space;(\mathbf{k}\right&space;)}{\exp\left&space;(&space;\frac{h\nu_{i}&space;\left&space;(\mathbf{k}\right&space;)&space;}{k_{B}T}&space;\right&space;)-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S&space;=&space;-k_{B}&space;\sum_{i,&space;\mathbf{k}}\ln&space;\left&space;[&space;1-\exp\left&space;(&space;\frac{-h\nu_{i}&space;\left&space;(\mathbf{k}\right&space;)&space;}{k_{B}T}&space;\right&space;)&space;\right&space;]&space;&plus;&space;\frac{h}{T}&space;\sum_{i,&space;\mathbf{k}}\,\frac{\nu_{i}&space;\left&space;(\mathbf{k}\right&space;)}{\exp\left&space;(&space;\frac{h\nu_{i}&space;\left&space;(\mathbf{k}\right&space;)&space;}{k_{B}T}&space;\right&space;)-1}" title="S = -k_{B} \sum_{i, \mathbf{k}}\ln \left [ 1-\exp\left ( \frac{-h\nu_{i} \left (\mathbf{k}\right ) }{k_{B}T} \right ) \right ] + \frac{h}{T} \sum_{i, \mathbf{k}}\,\frac{\nu_{i} \left (\mathbf{k}\right )}{\exp\left ( \frac{h\nu_{i} \left (\mathbf{k}\right ) }{k_{B}T} \right )-1}" /></a>

 ![Data flow](https://github.com/DavidCdeB/QHA/blob/master/G_donw.png)

In the athermal limit, the pressure is the derivative of the energy with respect to the volume, and the resultant expression is called an Equation of State (EOS), that can be fitted, for instance, to the Birch-Murnagan EOS.

However, at a finite temperature the pressure is no longer the derivative of the energy with respect to the volume but the derivative of the Helmholtz free energy:

![Data flow](https://github.com/DavidCdeB/QHA/blob/master/P_finite.png)
 
where the vibrational frequencies (called phonons in a periodic system) depend on the volume of the cell. These can be fitted quadratically:
 
 ![Data flow](https://github.com/DavidCdeB/QHA/blob/master/quadratic.png)
 
 So that:
 
 ![Data flow](https://github.com/DavidCdeB/QHA/blob/master/derivative.png)
 
 # 2. Power of the quasi-harmonic approximation
 
 If we represent the Gibbs free energy as a function of temperature and pressure for different thermodynamic polymorphs, we can obtain surface plots like the following:
 
 ![Data flow](https://github.com/DavidCdeB/QHA/blob/master/gibbs_free_energy_of_two_phase.jpg)
 
 where the crossing between two phases (alpha and beta in the figure) define a line, which is the phase boundary of these two phases in a 2D Temperature-Pressure diagram. In other words, by implementing the quasi-harmonic approximation we are predicting the **phase diagram** of a substance and the **thermodynamic stability** of different polymorphs, which leads to the exploration of **phase transitions** at a fnite temperature and pressure.
 
 # 2. What is the `QHA` program ? 
 
 `QHA` is a program for computational chemistry and physics that performs the quasi-harmonic approximation reading the frequencies at each volume calculated with [CRYSTAL](http://www.crystal.unito.it/index.php). 
 
 * Extracts all the frequencies within all the **k** points in the supercell
 * Fits the frequency of each normal mode with respect to the volume.
 * Calculates the pressure at finite temperature, as well as the entropy, heat capacity and Gibbs free energy
 * Produces tables summarizing the results for all the volumes analyzed
 * 3D surface plot of the Gibbs free energy as a function of Pressure and Temperature 
 
 The program is given as a `QHA.zip` file. When unzipped in the working directory, the program is structured as follows:
 
 * A master program ``QHA.py``
 * A series of ``bash`` and ``awk`` scripts for parsing data more effectively.
 * `gnuplot` scripts for the plotting of the surfaces.
 
 
 # 3. Files needed for running `QHA`:
 
 `QHA` requires two types of output files from CRYSTAL in the working directory:
 
 * The output from the `EOS` calulation: 
 
 ```
 EOS
[Optional sub-keywords]
END 
```
The name of this output has to end as `*EOS.out`

 * If the `EOS` calculation was performed over 11 volumes (the default), you should run 11 `SCELPHONO` outputs:
 
 ```
SCELPHONO
[supercell-matrix]
FREQCALC
NOINTENS
NOOPTGEOM
DISPERSI
RESTART
TEMPERAT
[range-of-temperatures-desired]
END
END
```
The name of all these 11 outputs have to end as `*T.out`

# 4. How to run `QHA`:

# Why `QHA` is useful ?

* The actual version of [CRYSTAL14 v1.0.4](http://www.crystal.unito.it/index.php). does not perform an automated quasi-harmonic approximation calculation.

* The upcoming version of CRYSTAL17 does perform an atomated quasi-harmonic approximation calculation for a given set of volumes. Unfortunalety, the optimization at a constant volume is performed within the supercell scheme. If the supercell is big, (as it should be in order to ensure convergence of the entropy - see point X), this might lead to unwanted phase transitions (Fig. CC). 
 Ideally, the optimization should have to be done in the the primitive cell prior to making the supercell for the phonons calculation, but this is not so trivial to implement in the code.




# 1. What is the quasi-harmonic approximation ?

Since the birth of quantum chemistry, almost every calculation was performed in the athermal limit (0K) and no pressure effects were considered (0Pa).
One of the most exciting challenges in an _ab intio_ calculation is to obtain information of the system at a finite temperature and pressure. This allow us to obtain a more realistic picture of the system in the everyday world, where temperature and pressure cannot be neglected and are indeed the driving force for many transformations in nature.

One of the most famous techniques for taking into account the effect of the temperature in the computed properties of molecules and crystals is _ab intio_ molecular dynamics [1, 2, 3], in which the Schrodinger equation is solved at each MD time step within the Born-Oppenheimer approximation. Unfortunetely, this is a very computationally expensive technique. Therefore, there is a huge interest in developing accurate and reliable models for the inclusion of the temperature in the standard first-principles quantum chemical methods.

The quasi-harmonic approximation is an elegant way to tacke with this problem in condensed matter, by considering each atom as an independent harmonic oscillator:

![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Images_for_README_md/levels_vibrat_cropped.png)

For a given independent harmonic oscillator, by summing over all these levels it is possible to derive the partition function:

![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Images_for_README_md/Zik_3.png)

where there is a value of frequency for each **k** vector. In a molecule, this is equivalent to a unique value of *k* (the Gamma point).

It is not difficult to derive the Helmholtz free energy, entropy and Gibbs free energy:

![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Images_for_README_md/F_2.png)

 ![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Images_for_README_md/entropy.png)
 
 ![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Images_for_README_md/G_2.png)

In the athermal limit, the pressure is the derivative of the energy with respect to the volume, and the resultant expression is called an Equation of State (EOS), that can be fitted, for instance, to the Birch-Murnagan EOS.

However, at a finite temperature the pressure is no longer the derivative of the energy with respect to the volume but the derivative of the Helmholtz free energy:

![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Images_for_README_md/P_finite.png)
 
where the vibrational frequencies (called phonons in a periodic system) depend on the volume of the cell. These can be fitted quadratically:
 
 ![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Images_for_README_md/quadratic.png)
 
 So that:
 
 ![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Images_for_README_md/derivative.png)
 
 # 2. Power of the quasi-harmonic approximation
 
 If we represent the Gibbs free energy as a function of temperature and pressure for different thermodynamic polymorphs, we can obtain surface plots like the following:
 
 ![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Images_for_README_md/gibbs_free_energy_of_two_phase.jpg)
 
 where the crossing between two phases (alpha and beta in the figure) define a line, which is the phase boundary of these two phases in a 2D Temperature-Pressure diagram. In other words, by implementing the quasi-harmonic approximation we are predicting the **phase diagram** of a substance and the **thermodynamic stability** of different polymorphs, which leads to the exploration of **phase transitions** at a fnite temperature and pressure.
 
 # 3. What is the `QHA` program ? 
 
 `QHA` is a program for computational chemistry and physics that performs the quasi-harmonic approximation reading the frequencies at each volume calculated with [CRYSTAL](http://www.crystal.unito.it/index.php). 
 
 * Extracts all the frequencies within all the **k** points in the supercell
 * Fits the frequency of each normal mode with respect to the volume.
 * Calculates the pressure at finite temperature, as well as the entropy, heat capacity and Gibbs free energy
 * Produces tables summarizing the results for all the volumes analyzed
 * 3D surface plot of the Gibbs free energy as a function of Pressure and Temperature 
 
The program was developed as part of my PhD project at [Prof. Nicholas Harrison's Computational Materials Science Group](http://www.imperial.ac.uk/computational-materials-science/people/), Imperial College London. The program was used to investigate the phase diagram and phase transitions mechanisms on the calcium carbonate system.

 
 # 4. Why is `QHA` useful ?

* The actual version of [CRYSTAL14 v1.0.4](http://www.crystal.unito.it/index.php). does not perform an automated quasi-harmonic approximation calculation.

* Fortunately, the upcoming version of CRYSTAL17 does perform an atomated quasi-harmonic approximation calculation for a given set of volumes. Unfortunalety, the optimization at a constant volume is performed within the supercell scheme. If the supercell is big, (as it should be in order to ensure convergence of the entropy), this might lead to several problems:

    * The optimization porcess is without doubt, more difficult in the supercell scheme: the cell is bigger, there are more atoms, and this can lead to convergence problems, or flase minima.

   * Not relevant (unwanted) supercell phase transitions. 
   
* Ideally, CRYSTAL should perform the optimization in the the primitive cell prior to making the supercell for the phonons calculation at a finite **k** point, but this is not so trivial to implement in the main code, according to the developers. Hopefully, this will be taken into account in future versions of the code. But for the moment, this `QHA` code is an easy and effective solution for evaluating thermodynamic properties of crystals at a finite temperature and pressure (the real world).

**_Note for more advanced users:_**

If you are wondering and concerned about FIXINDEX problems, there is no reason for that. With this `QHA` code, there are in fact two levels of FIXINDEX:

 * Since the code is reading from the `EOS.out`, the electronic energy `EL` is already "fixindexed" with respect to the equilibrium volume geometry.
 
 * Since the code is reading from each independent constant-volume frequency calculation, the frequencies for a given volume are "fixindexed" with respect to that specific volume, as opposed to the equilibrium volume geometry. This might appear to be a drawback, however, it happens to be an inmense advantage: since the frequencies are obtained from the second derivatives of the energy, we would obtain better eigenvalues and eigenvectors for that particular volume if the frequency calculation for a given volume is in fact "fixindexed" to that specific volume.
 
 
 # 5. Files needed for running `QHA`:
 
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
 Please ensure that you are using a sufficient big supercell for the entropy to be converged with the number of **k** points.

# 6. Data Flow

The input files needed, program scripts and results are summarized in this flow chart:

![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Images_for_README_md/Data_Flow4.png)


# 7. How to run `QHA`:

* `cd` to the working directory where you have the `*EOS.out` and the scelphono outputs `*T.out`
* Get the code: `git clone https://github.com/DavidCdeB/QHA`
* Give permissions to all the scripts: `chmod u+x *.sh *.py` 
* Run `QHA_master.py`

**_Prerequisites_**

To run, `QHA` requires Python with certain packages:

* Python 2.7 or higher.
    Packages: `numpy`, `scipy`, `re`, `os`, `glob`, `itertools`, `subprocess`, `sys` (All of these come with a default [Anacaonda](https://www.continuum.io/downloads) installation).

* Standard `bash` version in your system.

# 8. Test

Under the `Test` folder, you will find the `EOS.out` and 11 scelphono outputs `*T.out` for Calcite I.
If you run the program, you will obtain all the information explained in the Data flow, and in the last step,
the 3D surface plots shown in the Data Flow chart.

# 9. How to cite:

Please do cite the following reference when using this code:

de Busturia, D.C., Mallia, G. and Harrison, N. M. "Computed phase stability and phase transition mechanisms in CaCO3 at finite temperature and pressure" _In progress_

# 10. Contributing

`QHA` is free software released under the Gnu Public Licence version 3. 
All contributions to improve this code are more than welcome.

* Have a look at GitHub's ["How to contribute"](https://guides.github.com/activities/contributing-to-open-source/#contributing).

* If you are familiar with `git`: fork this repository and submit a pull request.

* If you are not familiar with `git`: 

    * If something should be improved, open an issue here on GitHub
    * If you think a new feature would be interested, open an issue
    * If you need a particular feature for your project contact me directly.
  
  # References
  
  [1] R. Car, M. Parrinello, Phys. Rev. Lett. 1985, 55, 2471
  
  [2] F. Buda, R. Car, M. Parrinello, Phys. Rev. B 1990, 41, 1680
  
  [3] F. D. Vila, V. E. Lindahl, J. J. Rehr, Phys. Rev. B 2012, 85, 024303

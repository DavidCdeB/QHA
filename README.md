# What is the quasi-harmonic approximation ?

Since the birth of quantum chemistry, almost every calculation was performed in the athermal limit (0K) and no pressure effects were considered (0Pa).
One of the most exciting challenges in an _ab intio_ calculation is to obtain information of the system at a finite temperature and pressure. This allow us to obtain a more realistic picture of the system in the everyday world, where temperature and pressure cannot be neglected and are indeed the driving force for many transformations in nature.

One of the most famous techniques for taking into account the effect of the temperature in the computed properties of molecules and crystals is _ab intio_ molecular dynamics [], in which the Schrodinger equation is solved at each MD time step within the Born-Oppenheimer approximation. Unfortunetely, this is a very computationally expensive technique. Therefore, there is a huge interest in developing accurate and reliable models for the inclusion of the temperature in the standard first-principles quantum chemical methods.

The quasi-harmonic approximation is an elegant way to tacke with this problem in condensed matter, by considering each atom as an independent harmonic oscillator:

![Data flow](https://github.com/DavidCdeB/QHA/blob/master/levels_vibrat_cropped.png)

By summing over all these levels of each independent harmonic oscillator, it is possible to derive the partition function:

![Data flow](https://github.com/DavidCdeB/QHA/blob/master/Z_i_k.png)

where there is a value of frequency for each *k* vector. In a molecule, this is equivalent to a unique value of *k* (the Gamma point).

, where the vibrational frequencies (called phonons in a periodic system) depend on the volume of the cell.



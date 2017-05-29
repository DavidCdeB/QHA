# What is the quasi-harmonic approximation ?

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
 
 

 where the vibrational frequencies (called phonons in a periodic system) depend on the volume of the cell.

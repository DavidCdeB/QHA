# 
# QHA program. David Carrasco de Busturia, 30 April 2017 
# Please read the documentation and istructions on: https://github.com/DavidCdeB/QHA
# This program is under the GNU General Public License v3.0. 
# davidcarrascobustur@gmail.com
# d.carrasco-de-bsuturia@imperial.ac.uk

import re
import os
import glob
from itertools import islice
import numpy as np
import subprocess
import itertools
import sys


# Obtaining the number of scelphono outputs in the working directory :
n_volume = []
path='./'
template = os.path.join(path, '*T.out')

for fname in glob.glob(template):
  print fname
  n_volume.append(fname) 

n_volume = len(n_volume)

# Obtaining the number of temperature points :
path='./'
template = os.path.join(path, '*T.out')

for fname in glob.glob(template):
  print fname
  f = open(fname, 'r')
  for line in f:

        if re.match(r"^ TEMPERATURE FOR THERMO ANALYSIS", line):
         start = line.find('POINTS') + 6 
         end = line.find(')') 
         result = line[start:end]

n_T = result
n_T = float(n_T)
n_T = int(float(n_T))


# Setting the number of formula units as a raw_input:
n_F_u = raw_input("""

Please type as an integer the number of formula units in the primitive cell. 
For example, Calcite I contains 2 formula units in the primitive (rombohedral) cell and 6 formula units in the crystallographic (hexagonal) cell. Thus, the number to be introduced is:   2 <and press ENTER>

""")

n_F_u = float(n_F_u)
n_F_u = int(float(n_F_u))


# Extracting BIRCH-MURNAGHAN 1947 parameters from the EOS output:
path='./'
template = os.path.join(path, '*EOS.out')


for fname in glob.glob(template):
  print fname
  f = open(fname, 'r')
  real_part = False

  for line in f:

        if re.match(r"^ BIRCH-MURNAGHAN 1947", line):
                  
                  parameters = line
                  p = parameters.split()
                  V0 = p[2]
                  E0 = p[3]
                  B0 = p[4]
                  B0_prime = p[5]

V0 = float(V0)

B0 = float(B0)
E0 = float(E0)
B0_prime = float(B0_prime)


# Extracting the number of modes ( name of variable = "factor" ):
path='./'
template = os.path.join(path, '*T.out')

for fname in glob.glob(template):
  print fname
  f = open(fname, 'r')
  real_part = False

  for line in f:

        if re.match(r"^  THERMODYNAMICAL PROPERTIES ARE CALCULATED AS A SUM OVER", line):

                  parameters = line
                  p = parameters.split()
                  factor = p[8]

factor = int(factor)


# Extracting the number of k-points ( name of variable = "N_k" ):
path='./'
template = os.path.join(path, '*T.out')

for fname in glob.glob(template):
  print fname
  f = open(fname, 'r')
  real_part = False

  for line in f:

        if re.match(r"^ \* THAT PERMITS THE CALCULATION OF MODES AT", line):

                  parameters = line
                  p = parameters.split()
                  N_k = p[8]

N_k = int(N_k)

# Extracting each thermodynamic variable:
Temperatures = []
ET = []
TS = []
EL = []
E0 = []
ENTROPY = []
VOLUME_EACH = []
VOLUME = []
HEAT_CAPACITY = []
ALL_FREQ = []
TOTAL = []
MODE_NUMBER = []

for fname in glob.glob(template):
  print fname
  f = open(fname, 'r')
  real_part = False

  def read_real_parts(fname):
    for line in f:

        if re.match(r"^ ET            :", line):
         start = line.find(':') + 8
         end = line.find(':') + 22
         result_ET = line[start:end]
         ET.append(result_ET)

        if re.match(r"^ TS            :", line):
         start = line.find(':') + 8
         end = line.find(':') + 22
         result_TS = line[start:end]
         TS.append(result_TS)

        if re.match(r"^ EL            :", line):
         start = line.find(':') + 4
         end = line.find(':') + 22
         result_EL = line[start:end]
         EL.extend([result_EL] * n_T)

        if re.match(r"^ E0            :", line):
         start = line.find(':') + 8
         end = line.find(':') + 22
         result_E0 = line[start:end]
         E0.extend([result_E0] * n_T)

        if re.match(r"^ ENTROPY       :", line):
         start = line.find(':') + 8
         end = line.find(':') + 22
         result_ENTROPY = line[start:end]
         ENTROPY.append(result_ENTROPY)

        if re.match(r"^ AT \(T =", line):
         start = line.find('T =') + 4
         end = line.find('K')
         result_Temperatures = line[start:end]
         Temperatures.append(result_Temperatures)

        if re.match(r"^ HEAT CAPACITY :", line):
         start = line.find(':') + 8
         end = line.find(':') + 22
         result_HEAT_CAPACITY = line[start:end]
         HEAT_CAPACITY.append(result_HEAT_CAPACITY)

        if '       A          B          C        ALPHA      BETA     GAMMA        VOLUME' in line:  # ok, for prim vols.

                  each_volume_times_4 = []
                  each_volume_times_100 = []
                  
                  parameters = (''.join(islice(f, 1)))
                  columns = parameters.split()
                  each_volume = columns[6]
                  print 'each_volume = ', each_volume

                  each_volume_times_4.extend([each_volume] * factor)  
                  each_volume_times_100.extend([each_volume] * n_T)  
                  
                  TOTAL.extend(each_volume_times_4)
                  VOLUME.extend(each_volume_times_100)

                  one_to_factor = range(1,factor+1)
                  MODE_NUMBER.extend(one_to_factor)
               
                  VOLUME_EACH.append(each_volume)

        if line.startswith(' REAL PART'):
            real_part = True
        elif line.startswith(' NORMAL MODES NORMALIZED TO CLASSICAL AMPLITUDES'):
            real_part = True
        elif line.startswith(' IMAGINARY PART'):
            real_part = False
        elif line.startswith(' FREQ(') and real_part:
            FREQS = line.split()
            del FREQS[0]
            yield FREQS

  FREQ = read_real_parts(fname) # gives you the generator
  All_frequencies = list(itertools.chain.from_iterable(FREQ))

  ALL_FREQ.extend(All_frequencies)

thing = '0.00'
while thing in ALL_FREQ: ALL_FREQ.remove(thing)

output_array_2 = np.vstack((TOTAL, ALL_FREQ, MODE_NUMBER)).T
np.savetxt('Volume_for_freqs_isolation_3_true_problem.dat', output_array_2, header="VOLUME (A^3/CELL) \t FREQS (CM^-1) \t mode number:", fmt="%s")

output_array = np.vstack((VOLUME, EL, E0, ET, ENTROPY, TS, HEAT_CAPACITY, Temperatures)).T
np.savetxt('Thermo_functions_2.dat', output_array, header="VOLUME (A^3/CELL) \t  EL (AU/CELL) \t  E0 (AU/CELL) \t  ET (AU/CELL) \t  ENTROPY (mHARTREE/(CELL*K))  TS (AU/CELL)  HEAT_CAPACITY (mHARTREE/(CELL*K))  Temperatures (K)", fmt="%s")


# Generating the "mode_X.dat" files:
print """ Generating the "mode_X.dat" files ..."""

for f in glob.glob("mode_*.dat"):
   os.remove(f)
handles = dict()

f_2 = open('Volume_for_freqs_isolation_3_true_problem.dat', 'r')
next(f_2)
s = set()
title_line = "# Volume \t Frequency \t Mode number\n"

for line in f_2:
   toks = line.split()
   filename = "mode_{}.dat".format(toks[-1])

   with open(filename,"a") as f:
      if filename in s:
         pass
      else:
        s.add(filename)
        f.write(title_line)

      f.write(line)


print line


# Quadratic fit:
print """ Analysing frequencies with respect to volume ..."""

path='./'
template = os.path.join(path, 'mode*')

parameters = []
valid_modes = []

for fname in glob.glob(template):

 VOLUME, Frequency, mode = np.loadtxt(fname, skiprows=1).T

 c, d, f = np.polyfit(VOLUME, Frequency, 2)

 output_array = np.vstack((c, d, f)).T
 output_array_1D = output_array.ravel()

 parameters.append(output_array_1D)

 valid_modes.append(mode[0])

for i,(arr,t) in enumerate(zip(parameters,valid_modes)):
    parameters[i] = np.append(arr,t)



np.savetxt('done_modes.dat', parameters, header="Frequency = c*VOLUME**2 + d*VOLUME + f; c \t d  \t f \t mode", fmt="%0.13f")

# Now, sort the file:

subprocess.call("./sort_the_file.sh", shell=True)

# Calculaing G:
print """ Calculating pressure at a finite temperautre ..."""
print """ Calculating Gibbs free energy ..."""

c1, d, f, mode = np.loadtxt('done_modes_sorted.dat', skiprows = 1).T
VOLUMES_REPEATED,  FREQ, modes = np.loadtxt('Volume_for_freqs_isolation_3_true_problem.dat',  skiprows = 1).T


################### CONSTANTS   ###############

# KB = boltmann cte, KB = 1.38064852(79)x10-23 J/K
KB = 1.38064852E-23

# h = plank constant, h = 6.626070040(81)x10-34 J s
h = 6.626070040E-34

# T = temperature, T = 298.15 K
#T = 10

# c = speed of light, c = 2.99792458E8 m/s
speed_of_light = 2.99792458E+8

VOLUME = VOLUME_EACH

VOLUME = [float(i) for i in VOLUME] # convert 11 volumes to floats to call the function


for i_VOLUME in VOLUME:
 print 'i_VOLUME each one= ', i_VOLUME


def P(V): 
    f0=(3.0/2.0)*B0
    f1=((V0/V)**(7.0/3.0))-((V0/V)**(5.0/3.0))
    f2=((V0/V)**(2.0/3.0))-1
    pressure= f0*f1*(1+(3.0/4.0)*(B0_prime-4)*f2)
    return pressure # This definition of "pressure" is internal to the function/

# TEST for MgO in a QHA calculation (4 points):
V = 144.76 # / (2**3)

#Temperatures_10_to_2000K = Temperatures[:100] 
Temperatures_10_to_2000K = Temperatures[:n_T] 

P1_in_GPa = []

for i_VOLUME in VOLUME:

 P_at_each_volume_T_0K_in_GPa = P(i_VOLUME)

 P1_in_GPa.append(P_at_each_volume_T_0K_in_GPa)

n_mode = factor

c, d, f, mode = np.loadtxt('done_modes_sorted.dat', skiprows = 1).T
V, FREQ, mode = np.loadtxt('Volume_for_freqs_isolation_3_true_problem.dat',  skiprows = 1).T

Temperatures_10_to_2000K = [float(i) for i in Temperatures_10_to_2000K]


V = V.reshape(n_volume, n_mode)

FREQ = FREQ.reshape(n_volume, n_mode)


P_for_each_volume_and_each_T = []
for i in range(n_volume):
  for j in range(n_T):
   P = 0
   for k in range(n_mode):

        P +=  (  0.5 + ( (np.exp(h *  FREQ[i,k] * 1E+2 * speed_of_light  / (KB*Temperatures_10_to_2000K[j])) - 1)**(-1) )  ) *  h * (2 * V[i,k] * c[k] + d[k]) *  1E+2 * speed_of_light * 1E+30 * 1E-9 
        
   P_for_each_volume_and_each_T.append(P)

P1_in_GPa = np.asarray(P1_in_GPa)


P_for_each_volume_and_each_T = np.asarray(P_for_each_volume_and_each_T)

P1_in_GPa = np.repeat(P1_in_GPa,n_T)


P_for_each_volume_and_each_T_divided_by_N_k = P_for_each_volume_and_each_T / N_k


P = P1_in_GPa -  P_for_each_volume_and_each_T_divided_by_N_k


VOLUME, EL, E0, ET, ENTROPY, TS, HEAT_CAPACITY, Temperatures_10_to_2000K = np.loadtxt('Thermo_functions_2.dat', skiprows = 1).T

output_array = np.vstack((VOLUME, P, EL, E0, ET, ENTROPY, TS, HEAT_CAPACITY, Temperatures)).T
np.savetxt('Thermo_functions_with_P.dat', output_array, header="VOLUME (A^3/CELL)  P (GPa)  \t EL (AU/CELL) \t  E0 (AU/CELL) \t  ET (AU/CELL) \t  ENTROPY (mHARTREE/(CELL*K))  TS (AU/CELL)  HEAT_CAPACITY (mHARTREE/(CELL*K))  Temperatures (K)", fmt="%s")


VOLUME, P, EL, E0, ET, ENTROPY, TS, HEAT_CAPACITY, Temperatures_10_to_2000K = np.loadtxt('Thermo_functions_with_P.dat', skiprows = 1).T

F = EL + E0 + ET - Temperatures_10_to_2000K * ENTROPY * 1E-3


PV = P * (VOLUME) * 1E+9 * 1E-30 * (1/(4.3597482E-18))   # Previous formula (correct)


G = EL + E0 + ET + PV - Temperatures_10_to_2000K * ENTROPY * 1E-3

output_array = np.vstack((VOLUME, P1_in_GPa, P_for_each_volume_and_each_T, P_for_each_volume_and_each_T_divided_by_N_k, P, EL, E0, ET, ENTROPY, TS, HEAT_CAPACITY, G, Temperatures_10_to_2000K)).T
np.savetxt('Thermo_functions_with_both_contributions_to_P_and_G.dat', output_array, header="VOLUME (A^3/CELL)  P1_in_GPa  P2_in_Gpa  P2_in_Gpa_divided_by_N_k(GPa)   P (GPa)  \t EL (AU/CELL) \t  E0 (AU/CELL) \t  ET (AU/CELL) \t  ENTROPY (mHARTREE/(CELL*K))  TS (AU/CELL)  HEAT_CAPACITY (mHARTREE/(CELL*K))  G  (mHARTREE/CELL)   Temperatures (K)", fmt="%0.13f")


output_array = np.vstack((VOLUME, P1_in_GPa, P, EL, E0, ET, ENTROPY, TS, HEAT_CAPACITY, G, Temperatures_10_to_2000K)).T
np.savetxt('Thermo_functions_with_P_and_G.dat', output_array, header="VOLUME (A^3/CELL)  P1_in_GPa  P (GPa)  \t EL (AU/CELL) \t  E0 (AU/CELL) \t  ET (AU/CELL) \t  ENTROPY (mHARTREE/(CELL*K))  TS (AU/CELL)  HEAT_CAPACITY (mHARTREE/(CELL*K))  G  (mHARTREE/CELL)   Temperatures (K)", fmt="%0.13f")

subprocess.call("./sort_Thermo.sh", shell=True)


### Extracting EL from EOS output:

path='./'
template = os.path.join(path, '*EOS.out')



for fname in glob.glob(template):
  print fname
  f = open(fname, 'r')
  real_part = False

  for line in f:

        if 'SORTING VOLUMES/ENERGIES' in line:  
                  f.next()
                  f.next()
                  f.next()
                  parameters = (''.join(islice(f, 11)))

                  both = parameters.splitlines()

                  for i in both:
                      both_splitted = i.split()

                  again = []
                  for i in both:
                      sure = i.split()
                      again.append(sure)

                  VOLUME_EOS = []
                  for i in range(len(again)):
                      vol = again[i][0]
                      VOLUME_EOS.append(vol)

                  EL_EOS = []
                  for j in range(len(again)):
                      energy = again[j][1]
                      EL_EOS.append(energy)


# task: multiply each by n_T

### Repeating each EL_EOS and VOLUME_EOS by n_T = 100 :
EL_EOS  = np.repeat(EL_EOS,n_T)
VOLUME_EOS  = np.repeat(VOLUME_EOS,n_T)

# Save this just in case:
output_array = np.vstack((VOLUME_EOS, EL_EOS)).T
np.savetxt('VOLUME_EOS_and_EL_EOS.dat', output_array, header="VOLUME_EOS (A^3/CELL)  EL_EOS (AU/CELL)", fmt="%s")

# Then, calculation of G with EL_EOS:
VOLUME_EOS, EL_EOS = np.loadtxt('VOLUME_EOS_and_EL_EOS.dat', skiprows = 1).T
VOLUME, P1_in_GPa, P, EL, E0, ET, ENTROPY, TS, HEAT_CAPACITY, G, Temperatures_10_to_2000K = np.loadtxt('Thermo_functions_with_P_and_G_sorted.dat', skiprows = 1).T


F_with_EL_EOS = EL_EOS + E0 + ET - Temperatures_10_to_2000K * ENTROPY * 1E-3

PV = P * (VOLUME) * 1E+9 * 1E-30 * (1/(4.3597482E-18))   # Previous formula (correct)

G_with_EL_EOS = EL_EOS + E0 + ET + PV - Temperatures_10_to_2000K * ENTROPY * 1E-3

print """ Plotting ..."""


output_array = np.vstack((VOLUME, P1_in_GPa, P, EL_EOS, E0, ET, ENTROPY, TS, HEAT_CAPACITY, G_with_EL_EOS, Temperatures_10_to_2000K)).T
np.savetxt('Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS.dat', output_array, header="VOLUME (A^3/CELL)  P1_in_GPa  P (GPa)  \t EL_EOS (AU/CELL) \t  E0 (AU/CELL) \t  ET (AU/CELL) \t  ENTROPY (mHARTREE/(CELL*K))  TS (AU/CELL)  HEAT_CAPACITY (mHARTREE/(CELL*K))  G_with_EL_EOS  (mHARTREE/CELL)   Temperatures (K)", fmt="%0.13f")

VOLUME_per_n_F_u = VOLUME/n_F_u
EL_EOS_per_n_F_u = EL_EOS/n_F_u
E0_per_n_F_u = E0/n_F_u
ET_per_n_F_u = ET/n_F_u
ENTROPY_per_n_F_u = ENTROPY/n_F_u
TS_per_n_F_u = TS/n_F_u
HEAT_CAPACITY_per_n_F_u = HEAT_CAPACITY/n_F_u
G_with_EL_EOS_per_n_F_u = G_with_EL_EOS/n_F_u

output_array = np.vstack((VOLUME_per_n_F_u, P1_in_GPa, P, EL_EOS_per_n_F_u, E0_per_n_F_u, ET_per_n_F_u, ENTROPY_per_n_F_u, TS_per_n_F_u, HEAT_CAPACITY_per_n_F_u, G_with_EL_EOS_per_n_F_u, Temperatures_10_to_2000K)).T
np.savetxt('Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS__VOLUME_and_All_energies_divided_by_F_unit.dat', output_array, header="VOLUME_per_n_F_u (A^3/CELL)  P1_in_GPa  P (GPa)  \t EL_EOS_per_n_F_u (AU/CELL) \t  E0_per_n_F_u (AU/CELL) \t  ET_per_n_F_u (AU/CELL) \t  ENTROPY_per_n_F_u (mHARTREE/(CELL*K))  TS_per_n_F_u (AU/CELL)  HEAT_CAPACITY_per_n_F_u (mHARTREE/(CELL*K))  G_with_EL_EOS_per_n_F_u  (mHARTREE/CELL)   Temperatures (K)", fmt="%0.13f")


subprocess.call("./blocking_in_temperatures_more_effective_master_program.sh", shell=True)


subprocess.call("./temperature_splitting.sh", shell=True)

subprocess.call("./order_pallete_and_scatter_and_visualization.sh", shell=True)

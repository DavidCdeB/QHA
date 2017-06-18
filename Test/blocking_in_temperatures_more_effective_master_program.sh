#!/bin/bash
# Master program for blocking temperature-wise

# To sort in temperature-wise for adequate pallete ploting in gnuplot:
sort -k11 -n Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS__VOLUME_and_All_energies_divided_by_F_unit.dat  > Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS__VOLUME_and_All_energies_divided_by_F_unit_SORTED_in_Ts.dat  

# Calls this awk script to separate in blocks by an empty line every time the temperature changes:
awk -f help_spacing_in_temperatures_wise.awk < Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS__VOLUME_and_All_energies_divided_by_F_unit_SORTED_in_Ts.dat > Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS__VOLUME_and_All_energies_divided_by_F_unit_SORTED_in_Ts_blocked.dat

# substitute 1st (blank line) by the header form Thermo*_SORTED_in_Ts.dat:
var="# VOLUME_per_n_F_u (A^3/CELL)  P1_in_GPa  P (GPa)        EL_EOS_per_n_F_u (AU/CELL)       E0_per_n_F_u (AU/CELL)          ET_per_n_F_u (AU/CELL)          ENTROPY_per_n_F_u (mHARTREE/(CELL*K))  TS_per_n_F_u (AU/CELL)  HEAT_CAPACITY_per_n_F_u (mHARTREE/(CELL*K))  G_with_EL_EOS_per_n_F_u  (mHARTREE/CELL)   Temperatures (K)"
#var="oror"

# Because the $var contains "/", it does not work, e.g., if you try var="oror" We can use an alternate regex delimiter (~) as sed allows you to use any delimiter
sed "1s~.*~$var~" Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS__VOLUME_and_All_energies_divided_by_F_unit_SORTED_in_Ts_blocked.dat > Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS__VOLUME_and_All_energies_divided_by_F_unit_SORTED_in_Ts_blocked_with_header.dat  

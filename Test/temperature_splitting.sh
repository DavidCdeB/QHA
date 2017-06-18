#!/bin/bash
# This allows to split the *blocked_with_header.dat 
# file into n_T files, one per termperature.
awk -v RS= '{print > ("G_vs_P_at_Temperature_" NR )}' Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS__VOLUME_and_All_energies_divided_by_F_unit_SORTED_in_Ts_blocked_with_header.dat
bash moving.sh

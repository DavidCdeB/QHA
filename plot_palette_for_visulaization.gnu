#

#
#set termoption enhanced
#set encoding utf8 # uncomment to save eps


#set term post enh color eps # uncomment to save eps


#set output "Aragonite_plot_palette.eps" # uncomment to save eps


#set title "Calcite I"  font  ", 20"
set ylabel "Pressure (GPa)" font  ", 15" rotate parallel
set zlabel "Gibbs free energy/Formula Unit (a.u.)"  font  ", 13 "  offset -3,0,0  rotate parallel
set xlabel 'Temperature (K)' font  ", 15" offset -3,0,0  rotate parallel

#set xrange [124:138]
#set yrange [-1883.030:-1883.000]
set xtics font ", 15" # offset 0,1 border 1,1,1

set ytics font ", 15"
set key font ",15" # Changes the font of the letters of the legend

#set key outside
set ticslevel 0

set palette defined ( 0 "blue", 0.5 "light-grey", 1 "red" )

set grid
#set dgrid3d 30,30 gauss 
set view 60, 30, 1, 1
# splot "grid" using 1:2:3 with lp lt 1 pt 7  #point type YY

splot "Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS__VOLUME_and_All_energies_divided_by_F_unit_SORTED_in_Ts_blocked.dat" using 11:3:10 w pm3d title "" # option in the book
#splot "Thermo_functions_with_P_and_G_sorted_with_EL_from_EOS__VOLUME_and_All_energies_divided_by_F_unit.dat" using 11:3:10 with points lc 2 title "" #original scatter (green)

pause -1
#set output "Aragonite_plot_palette.eps" # uncomment to save eps

replot # uncomment to save eps


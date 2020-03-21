set EMP;
set SHIFT;

param Prefered{EMP, SHIFT};
param Cannot{EMP, SHIFT};
param dayhours{EMP};
param weekhour{EMP};

Var W{EMP, SHIFT} binary;

maximize Preference:
  sum{e in EMP, s in SHIFT} W[e,s]*Prefered[e,s];

subject to Shifts_Filled{s in SHIFT}:
  sum{e in EMP} W[e,s] = 1;

subject to weekhours{e in EMP}:
  sum{s in SHIFT} (2 * W[e,s]) = weekhour[e];

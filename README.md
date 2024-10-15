<img width="763" alt="diagram ieee9" src="https://github.com/user-attachments/assets/9544356d-9bc0-4205-a33d-9b85a78e4df0">
<body><p align="center"><i>IEEE 9-Bus Power System</i></p></body>

<br><br>

  This is a 24-hour load dispatch scenario in a standard IEEE 9-bus system, including three generators, three loads, and six transmission lines.

  Synthetic data is supplied for load profiles based on general trends in load demand throughout the day, and fixed percentages of total generation power are dispatched between the generators. 
50% load demand for generator 1, 30% for generator 2, and 20% for generator 3.

  Power flow is solved at each hour to ensure that load and generation are balanced, and that the system operates within its constraints. Generator dispatch and bus voltage data are recorded at each time step. Transmission line flow data is retrieved as well, including active and reactive power in both directions to account for line losses. Case data is saved for each hour.


  Sample output for one hour:

  <br>
<pre>
  <code>

Running hour 24

Power flow data changed for load "1" at bus 5 [BUS5        230.00]:
X--ORIGINAL--X  X-NEW VALUE--X  DATA ITEM
    55.0000         50.0000      PL

Power flow data changed for load "1" at bus 6 [BUS6        230.00]:
X--ORIGINAL--X  X-NEW VALUE--X  DATA ITEM
    50.0000         45.0000      PL

Power flow data changed for load "1" at bus 8 [BUS8        230.00]:
X--ORIGINAL--X  X-NEW VALUE--X  DATA ITEM
    55.0000         50.0000      PL

Power flow data changed for machine "1" at bus 1 [BUS1        16.500]:
X--ORIGINAL--X  X-NEW VALUE--X  DATA ITEM
    80.8008         72.5000      PG

Power flow data changed for machine "1" at bus 2 [BUS2        18.000]:
X--ORIGINAL--X  X-NEW VALUE--X  DATA ITEM
    48.0000         43.5000      PG

Power flow data changed for machine "1" at bus 3 [BUS3        13.800]:
X--ORIGINAL--X  X-NEW VALUE--X  DATA ITEM
    32.0000         29.0000      PG

ITER       DELTAP      BUS         DELTAQ      BUS        DELTA/V/      BUS       DELTAANG      BUS
 0         0.0500(      6     )    0.0000(      4     )
                                                           0.00111(      6     )   0.00807(      6     )      
 1         0.0001(      6     )    0.0003(      4     )
                                                           0.00002(      5     )   0.00002(      8     )      
 2         0.0000(      4     )    0.0000(      4     )


Reached tolerance in 2 iterations

Largest mismatch:     -0.00 MW      0.00 Mvar      0.00 MVA at bus 4 [BUS4        230.00]
System total absolute mismatch:                    0.00 MVA

SWING BUS SUMMARY:
 BUS#-SCT X-- NAME --X BASKV      PGEN     PMAX    PMIN      QGEN     QMAX    QMIN
    1     BUS1        16.500      73.2    250.0    10.0       4.0    300.0  -300.0
    
Generator Dispatch for Hour 24
Generator at Bus 1: 73.17 MW
Generator at Bus 2: 43.50 MW
Generator at Bus 3: 29.00 MW

Bus Voltages (p.u.):
Bus 1: 1.000 p.u.
Bus 2: 1.000 p.u.
Bus 3: 1.000 p.u.
Bus 4: 0.999 p.u.
Bus 5: 0.980 p.u.
Bus 6: 0.993 p.u.
Bus 7: 1.002 p.u.
Bus 8: 0.994 p.u.
Bus 9: 1.007 p.u.
Branch Flows (MW and Mvar):
Line from Bus 4 to Bus 5
  MW flow (From -> To): 37.84, MW flow (To -> From): -37.67
  Mvar flow (From -> To): 8.83, Mvar flow (To -> From): -7.34
Line from Bus 4 to Bus 6
  MW flow (From -> To): 35.33, MW flow (To -> From): -35.12
  Mvar flow (From -> To): -7.89, Mvar flow (To -> From): 9.04
Line from Bus 5 to Bus 7
  MW flow (From -> To): -12.33, MW flow (To -> From): 12.42
  Mvar flow (From -> To): -25.43, Mvar flow (To -> From): 25.87
Line from Bus 6 to Bus 9
  MW flow (From -> To): -9.88, MW flow (To -> From): 9.93
  Mvar flow (From -> To): -23.37, Mvar flow (To -> From): 23.60
Line from Bus 7 to Bus 8
  MW flow (From -> To): 31.08, MW flow (To -> From): -30.99
  Mvar flow (From -> To): 0.32, Mvar flow (To -> From): 0.42
Line from Bus 8 to Bus 9
  MW flow (From -> To): -19.01, MW flow (To -> From): 19.07
  Mvar flow (From -> To): -20.58, Mvar flow (To -> From): 21.05

Case saved in file C:\Users\todst\ieee9_hour_24.sav on MON, OCT 14 2024  19:15

</code>
</pre>

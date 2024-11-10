import psspy # type: ignore
psspy.psseinit(9) 
psspy.case('IEEE-9.sav')

#Flat start Gauss-Seidel solution
psspy.solv([0,0,0,1,1,0])
#Non flat start Gauss-Seidel solution
psspy.solv([0,0,1,1,1,0])
#Non flat start Newton-Raphson solution x2
psspy.fdns([1,0,0,1,1,0,99,0])
psspy.fdns([1,0,0,1,1,0,99,0])

def generator_contingencies():
    psspy.dfax_2([0,1,0],r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.sub""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.mon""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\generators.con""",
    r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.dfx""")
    psspy.accc_with_dsp_3( 0.5,[0,0,0,1,1,2,0,0,0,0,0],r"""SAVNW""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.dfx""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.acc""","","","")
    psspy.accc_single_run_report_4([0,1,2,1,1,0,1,0,0,0,0,0],[0,0,0,0,6000],[ 0.5, 5.0, 100.0,0.0,0.0,0.0, 99999.],r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.acc""")

def transmission_line_contingencies():
    psspy.dfax_2([0,1,0],r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.sub""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.mon""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\transmission_lines.con""",
    r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.dfx""")
    psspy.accc_with_dsp_3( 0.5,[0,0,0,1,1,2,0,0,0,0,0],r"""SAVNW""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.dfx""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.acc""","","","")
    psspy.accc_single_run_report_4([0,1,2,1,1,0,1,0,0,0,0,0],[0,0,0,0,6000],[ 0.5, 5.0, 100.0,0.0,0.0,0.0, 99999.],r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.acc""")

def transformer_contingencies():
    psspy.dfax_2([0,1,0],r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.sub""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.mon""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\transformers.con""",
    r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.dfx""")
    psspy.accc_with_dsp_3( 0.5,[0,0,0,1,1,2,0,0,0,0,0],r"""SAVNW""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.dfx""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.acc""","","","")
    psspy.accc_single_run_report_4([0,1,2,1,1,0,1,0,0,0,0,0],[0,0,0,0,6000],[ 0.5, 5.0, 100.0,0.0,0.0,0.0, 99999.],r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.acc""")

def bus_contingencies():
    psspy.dfax_2([0,1,0],r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.sub""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.mon""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\buses.con""",
    r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.dfx""")
    psspy.accc_with_dsp_3( 0.5,[0,0,0,1,1,2,0,0,0,0,0],r"""SAVNW""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.dfx""",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.acc""","","","")
    psspy.accc_single_run_report_4([0,1,2,1,1,0,1,0,0,0,0,0],[0,0,0,0,6000],[ 0.5, 5.0, 100.0,0.0,0.0,0.0, 99999.],r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\ieee9.acc""")

def three_phase_short_circuit():
    #Run IEC fault calculation for Bus 2
    psspy.bsys(0,0,[ 13.8, 230.],0,[],1,[2],0,[],0,[])
    psspy.iecs_4(0,0,[1,0,0,0,2,0,1,0,0,3,2,2,0,0,0,2,0],[ 0.08333, 1.1],"","",r"""C:\Users\todst\OneDrive\Documents\PTI\PSSE34\test.sc""")
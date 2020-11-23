



import  rpy2.robjects.packages as rpkgs
import rpy2.robjects as ro


utils = rpkgs.importr('utils')
utils.chooseCRANmirror(ind=1) 
try:
    Dssat = rpkgs.importr("DSSAT")
except:
    package_name1 = "DSSAT"
    ro.r(f'install.packages("{package_name1}")')

def add_v_fmt():
    return Dssat.add_v_fmt
def as_DSSAT_tbl():
    return Dssat.as_DSSAT_tbl
def add_v_fmt(): 
    return Dssat.add_v_fmt
def as_DSSAT_tbl():
    return Dssat.as_DSSAT_tbl
def mutate_cond(): 
    return Dssat.mutate_cond
def read_cul():
    return Dssat.read_cul
def read_dssat():
    return Dssat.read_dssat
def read_dssbatch(): 
    return Dssat.read_dssbatch
def read_eco():
    return Dssat.read_eco
def read_filea(): 
    return Dssat.read_filea
def read_filet() :
    return Dssat.read_filet
def read_filex():
    return Dssat.read_filex
def read_output(): 
    return Dssat.read_output
def read_pest() :
    return Dssat.read_pest
def read_soil_profile():
    return Dssat.read_soil_profile
def read_sol(): 
    return Dssat.read_sol
def read_tier(): 
    return Dssat.read_tier
def read_wth():
    return Dssat.read_wth
def run_dssat(): 
    return Dssat.run_dssat
def write_cul(): 
    return Dssat.write_cul
def write_dssbatch(): 
    return Dssat.write_dssbatch
def write_eco():
    return Dssat.write_eco
def write_filea(): 
    return Dssat.write_filea
def write_filet(): 
    return Dssat.write_filet
def write_filex(): 
    return Dssat.write_filex
def write_sol(): 
    return Dssat.write_sol
def write_tier(): 
    return Dssat.write_tier
def write_wth(): 
    return Dssat.write_wth



print(help(add_v_fmt))




        
        
        






















